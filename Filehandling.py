

from openpyxl import load_workbook
with open(r"C:\Users\srina\OneDrive\Documents\Book1.xlsx",'+rb') as f:
    content = f.read()
    print(content)
    
from pypdf import PdfReader
with open(r"C:\Users\srina\OneDrive\Documents\Resume.pdf",'+rb') as f:
    content = f.read()
    print(content)
    
