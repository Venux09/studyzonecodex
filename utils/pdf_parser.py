import pdfplumber#a  python library which is used to extract text from the pdf

def extract_text(pdf_path):#simple function for extracting the text from the file and returning that to main/
    text = ""
    with  pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text+= page.extract_text()
            return text [:12000]#text limit
