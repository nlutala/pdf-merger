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

    def merge_pdfs(self, filename="merged_file.pdf") -> None:
        '''
        Params:
        filename (str) - a name for the new merged pdf
        '''
        for pdf in self.pdfs:
            if pdf.endswith(".pdf"):
                self.merger.append(pdf)
            else: # Else statement may be redundant as I check for this below.
                raise TypeError("Expected PDF file(s) but a file with another file extension was given instead.")
        
        # Create the file
        if filename.endswith(".pdf"):
            self.merger.write(filename)
        else:
            self.merger.write(f"{filename}.pdf")

        self.merger.close()
        
        base_dir = os.path.dirname(__file__)
        
        # Move the merged file into a new folder
        merged_files_path = os.path.join(base_dir, 'merged-files')
        
        if os.path.exists(merged_files_path):
            if filename in os.listdir(merged_files_path):
                count = [1 for file in os.listdir(merged_files_path) if file.startswith(filename[:len(filename)-4])]
                os.rename(os.path.join(base_dir, filename), 
                          os.path.join(merged_files_path, f"{filename[:len(filename)-4]}_{sum(count)}.pdf"))
        else:
            os.mkdir(merged_files_path)
            os.rename(os.path.join(base_dir, f"{filename[:len(filename)-4]}.pdf"), 
                      os.path.join(merged_files_path, f"{filename[:len(filename)-4]}.pdf"))
                
        # Move the original files into another folder
        original_files_path = os.path.join(base_dir, 'original-files')
        
        if not os.path.exists(original_files_path):
            os.mkdir(original_files_path)
        
        for file in os.listdir(base_dir):
            if file.endswith(".pdf"):
                try:
                    os.rename(os.path.join(base_dir, file), 
                            os.path.join(original_files_path, file))
                except FileExistsError:
                    os.remove(os.path.join(original_files_path, file))
                    os.rename(os.path.join(base_dir, file), 
                              os.path.join(original_files_path, file))

if __name__ == "__main__":
    print("PDF Merger Program\n")
    pdfs = []

    for file in os.listdir():
        if file.endswith(".pdf"):
            pdfs.append(file)

    merger = PDFMerger(pdfs)

    filename = input("Please enter the name you would like to call the new merged PDF file. \n(If this is left empty, the name of the new pdf file generated will be 'merged_file.pdf'): ")
    
    if filename == "":
        merger.merge_pdfs()
    else:
        merger.merge_pdfs(filename)
        