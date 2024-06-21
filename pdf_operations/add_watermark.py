import PyPDF2
import sys
import os

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    """
    Adds a watermark to each page of the input PDF file and saves the result to the output PDF file.

    Parameters:
    input_pdf (str): Path to the input PDF file.
    watermark_pdf (str): Path to the watermark PDF file.
    output_pdf (str): Path to the output PDF file.
    """
    try:
        with open(input_pdf, 'rb') as input_file, open(watermark_pdf, 'rb') as watermark_file:
            template = PyPDF2.PdfFileReader(input_file)
            watermark = PyPDF2.PdfFileReader(watermark_file)
            output = PyPDF2.PdfFileWriter()

            for i in range(template.getNumPages()):
                page = template.getPage(i)
                page.mergePage(watermark.getPage(0))
                output.addPage(page)

            with open(output_pdf, 'wb') as output_file:
                output.write(output_file)
                
            print(f"Watermarked PDF saved as: {output_pdf}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")
    except PyPDF2.utils.PdfReadError as e:
        print(f"Error reading PDF file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_watermark.py <input_pdf> <watermark_pdf> <output_pdf>")
    else:
        input_pdf = sys.argv[1]
        watermark_pdf = sys.argv[2]
        output_pdf = sys.argv[3]

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_pdf)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        add_watermark(input_pdf, watermark_pdf, output_pdf)

