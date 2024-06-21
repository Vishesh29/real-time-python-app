# Python code to add watermark in PDF

import PyPDF2

template = PyPDF2.PdfFileReader(open('images/merged_pdf.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('images/wtr.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('images/waterparked_output.pdf','wb') as file:
        output.write(file)


