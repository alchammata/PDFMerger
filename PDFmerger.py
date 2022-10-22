import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir): #pdfs are in the same directory as the .py file
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("Combined PDF file")
