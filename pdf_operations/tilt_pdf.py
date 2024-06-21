import PyPDF2
import sys
import os

def rotate_pdf(input_file, output_file):
    """
    Rotates the first page of the input PDF file by 90 degrees clockwise and saves it to the output file.

    Parameters:
    input_file (str): Path to the input PDF file.
    output_file (str): Path to the output PDF file.
    """
    try:
        with open(input_file, 'rb') as file:  # binary read mode
            reader = PyPDF2.PdfFileReader(file)
            if reader.isEncrypted:
                reader.decrypt('')  # Add password if encrypted, empty string for none

            print(f"Number of pages: {reader.numPages}")  # number of pages
            if reader.numPages < 1:
                raise ValueError("The input PDF has no pages.")

            page = reader.getPage(0)
            page.rotateClockwise(90)
            
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(page)
            
            with open(output_file, 'wb') as newfile:
                writer.write(newfile)
                
            print(f"Rotated PDF saved as: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PyPDF2.utils.PdfReadError as e:
        print(f"Error reading PDF file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tilt_pdf.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        rotate_pdf(input_file, output_file)
