import PyPDF2

with open('протирочная машина.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_page = pdf_reader.getPage(0)
    print(pdf_page.extractText())
    for page_num in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(page_num)
        print(pdf_page.extractText())
