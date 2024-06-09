'''
A class that merges a pdf inputted by a user
'''

from pypdf import PdfWriter
import os

class PDFMerger():
    def __init__(self, pdfs: list) -> None:
        '''
        Params:
        pdf (string) - list of pdf file names from the current directory of this script (pdf_merger.py)
        '''
        self.pdfs = pdfs
        self.base_dir = os.path.dirname(__file__)
        self.merged_files_path = os.path.join(self.base_dir, 'merged-files')
        self.original_files_path = os.path.join(self.base_dir, 'original-files')

        if len(self.pdfs) == 0:
            raise ValueError("There are no PDF files in this directory to merge.")
        elif len(self.pdfs) == 1:
            raise ValueError("There is only PDF file in this directory. There needs to be 2 or more PDF files in this directory to merge.")

        self.merger = PdfWriter()
        
    def _move_merged_file_to_merge_folder(self, filename: str) -> None:
        '''
        Moves the merged files into a folder called merged-files
        
        Params:
        filename (string)
        '''
        if filename.endswith(".pdf"):
            if os.path.exists(self.merged_files_path):
                if filename in os.listdir(self.merged_files_path):
                    count = [1 for file in os.listdir(self.merged_files_path) if file.startswith(filename[:len(filename)-4])]
                    os.rename(os.path.join(self.base_dir, filename), 
                              os.path.join(self.merged_files_path, f"{filename[:len(filename)-4]}_{sum(count)}.pdf"))
                else:
                    os.rename(os.path.join(self.base_dir, filename), 
                              os.path.join(self.merged_files_path, filename))
            else:
                os.mkdir(self.merged_files_path)
                os.rename(os.path.join(self.base_dir, filename), 
                          os.path.join(self.merged_files_path, filename))
        else:
            if os.path.exists(self.merged_files_path):
                if f"{filename}.pdf" in os.listdir(self.merged_files_path):
                    count = [1 for file in os.listdir(self.merged_files_path) if file.startswith(filename)]
                    os.rename(os.path.join(self.base_dir, f"{filename}.pdf"), 
                              os.path.join(self.merged_files_path, f"{filename}_{sum(count)}.pdf"))
                else:
                    os.rename(os.path.join(self.base_dir, f"{filename}.pdf"), 
                              os.path.join(self.merged_files_path, f"{filename}.pdf"))
            else:
                os.mkdir(self.merged_files_path)
                os.rename(os.path.join(self.base_dir, f"{filename}.pdf"), 
                          os.path.join(self.merged_files_path, f"{filename}.pdf"))
                
    def _move_original_files_to_original_folder(self) -> None:
        '''
        Moves the original files to a folder called original-files after
        they have been merged to make a merged pdf file.
        '''
        if not os.path.exists(self.original_files_path):
            os.mkdir(self.original_files_path)
        
        for file in os.listdir(self.base_dir):
            if file.endswith(".pdf"):
                try:
                    os.rename(os.path.join(self.base_dir, file), 
                              os.path.join(self.original_files_path, file))
                except FileExistsError:
                    os.remove(os.path.join(self.original_files_path, file))
                    os.rename(os.path.join(self.base_dir, file), 
                              os.path.join(self.original_files_path, file))

    def merge_pdfs(self, filename: str) -> None:
        '''
        Params:
        filename (str) - a name for the new merged pdf
        '''
        # Create the file
        if len(filename) == 0:
            filename = "merged_file.pdf"
        
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
        self._move_merged_file_to_merge_folder(filename)
        self._move_original_files_to_original_folder()
                    

if __name__ == "__main__":
    print("PDF Merger Program\n")
    pdfs = []

    for file in os.listdir():
        if file.endswith(".pdf"):
            pdfs.append(file)

    merger = PDFMerger(pdfs)

    filename = input("Please enter the name you would like to call the new merged PDF file. \n(If this is left empty, the name of the new pdf file generated will be 'merged_file.pdf'): ")
    merger.merge_pdfs(filename)
        