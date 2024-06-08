'''
A class that merges a pdf inputted by a user
'''

from pypdf import PdfWriter
import os

class PDFMerger():
    def __init__(self, pdfs: list) -> None:
        '''
        Params:
        pdf (string) - list of pdf file names
        '''
        self.pdfs = pdfs

        if len(pdfs) == 0:
            raise ValueError("There are no PDF files in this directory to merge.")
        elif len(pdfs) == 1:
            raise ValueError("There is only PDF file in this directory. There needs to be 2 or more PDF files in this directory to merge.")

        self.merger = PdfWriter()

    def merge_pdfs(self, filename="merged_file") -> None:
        '''
        Params:
        filename (str) - a name for the new merged pdf
        '''
        for pdf in self.pdfs:
            if pdf.endswith(".pdf"):
                self.merger.append(pdf)
            else: # Else statement may be redundant as I check for this below.
                raise TypeError("Expected PDF file(s) but a file with another file extension was given instead.")
        
        if filename.endswith(".pdf"):
            self.merger.write(filename)
        else:
            self.merger.write(f"{filename}.pdf")

        self.merger.close()

if __name__ == "__main__":
    print("PDF Merger Program\n")
    pdfs = []

    for file in os.listdir():
        if file.endswith(".pdf"):
            pdfs.append(file)

    merger = PDFMerger(pdfs)

    filename = input("Please enter the name you would like to call the new merged PDF file. \n(If this is left empty, the name of the new pdf file generated will be 'merged_file.pdf'): ")

    merger.merge_pdfs(filename)
