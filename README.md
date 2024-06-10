# pdf-merger
A script that combines multiple PDFs together to make 1 merged PDF.

## Description
This program was created to help me build on object-oriented programming concepts, automated testing as well as files and directories.

## Getting Started
### Dependencies
* Please ensure that you have Python version 3 installed on your computer. If you have not yet got the link, you can find the latest version of Python available using this link: https://www.python.org/downloads/

### Installing
* Open https://github.com/nlutala/pdf-merger/ in a new tab.
* Press the green "<> Code" button and press "Download ZIP"
* Once downloaded, extract all files to a new folder
* Open your preferred terminal (command prompt, windows powershell etc.) in the directory where the requirements.txt file is located and write: ``` pip install -r requirements.txt ```
* Now you should have all the required libraries to run the project

### Before executing the program
Ensure you have 2 or more PDF files in the directory the pdf_merger.py file is in (see example below). 
![pdf_merger_9](https://github.com/nlutala/pdf-merger/assets/87072306/b2722931-d504-439c-bf2c-9bd28a82853d)

It doesn't matter if you don't as the script is written to handle for these cases (see below)
![pdf_merger_1](https://github.com/nlutala/pdf-merger/assets/87072306/2a62ba5c-cf4a-414c-a67a-d04d6a744b06)

### Executing the program
* To run the script, write the following command in the terminal: ``` python pdf_merger.py ```
* You will then be presented with this screen and prompted to enter the name of the new merged file. ![pdf_merger_2](https://github.com/nlutala/pdf-merger/assets/87072306/fcfd173f-ceb0-4a0e-a5fe-85c90f36c075) ![pdf_merger_3](https://github.com/nlutala/pdf-merger/assets/87072306/4f3978df-042c-4909-8635-1b752fae791c)

* You will then be able to find this file in a new folder called "merged-files".![pdf_merger_4](https://github.com/nlutala/pdf-merger/assets/87072306/5c18a3d0-fdc6-4eb1-981f-1ffd3c26cd15)

* Your original PDF files will also be moved a new folder called "original-files". (I have used the same example PDF files you can find in the Tests/ folder) ![pdf_merger_5](https://github.com/nlutala/pdf-merger/assets/87072306/cfea2747-e6d3-4ce7-8a6b-57f1e8d7ff1c)


I hope this script is useful!

### Other comments
* While testing this script on my computer, I have found that merging some PDF files could result in text being printed to the terminal that you may not be expecting. This can be ignored as a new merged PDF file is generated. Here is an example of an instance of me of merging my old university lecture slides into one PDF. 
![pdf_merger_6](https://github.com/nlutala/pdf-merger/assets/87072306/26b3cca5-444e-4547-942b-64bc5be479f4)
![pdf_merger_7](https://github.com/nlutala/pdf-merger/assets/87072306/1388941e-90bb-439d-89cc-2748ddd1ad54)

* One small pointer would also be to perhaps number your PDFs if there is a specific order in how you would like them merged. This helps the pdf_merger preserve the same order in the final PDF it generates. For example, labelling three files file1.pdf, file2.pdf and file3.pdf will allow the pdf_merger to merge and create a PDF file showing the contents of file1.pdf, file2.pdf and then file3.pdf

### Author
Nathan Lutala, nlutala

## Version History
* 0.1 - First release

## Acknowledgements
Inspiration for writing this readme file
* https://github.com/nlutala/Hangman

