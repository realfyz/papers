import pdfplumber

with pdfplumber.open("./static/refs/MONE-Comments.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page)