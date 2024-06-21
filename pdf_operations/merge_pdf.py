# Python code to merge PDF
# Note: I am using PyPDF version as 3.0.1 so PdfFileMerger function is deprecated in this version.

import sys
import PyPDF2

def merge_pdfs(pdf1, pdf2, output='merged_pdf.pdf'):
    """
    Merges two PDF files into one.

    Parameters:
    pdf1 (str): Path to the first PDF file.
    pdf2 (str): Path to the second PDF file.
    output (str): Path to the output merged PDF file (default is 'merged_pdf.pdf').
    """
    try:
        merger = PyPDF2.PdfMerger()

        # Append the PDFs to the merger
        merger.append(pdf1)
        merger.append(pdf2)

        # Write out the merged PDF
        merger.write(output)
        print(f"Successfully merged '{pdf1}' and '{pdf2}' into '{output}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <pdf1> <pdf2>")
    else:
        pdf1 = sys.argv[1]
        pdf2 = sys.argv[2]
        merge_pdfs(pdf1, pdf2)
