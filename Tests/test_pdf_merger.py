'''
Tests for the pdf_merger script
'''

import os
import unittest
from pdf_merger import PDFMerger
from pypdf import PdfReader

class TestPDFMerger(unittest.TestCase):
    def test_valueerror_is_raised_if_number_of_pdfs_is_zero(self):
        pdfs = []
        with self.assertRaises(ValueError):
            merger = PDFMerger(pdfs)

    def test_valueerror_is_raised_if_number_of_pdfs_is_one(self):
        pdfs = ["example_file_1.pdf"]
        with self.assertRaises(ValueError):
            merger = PDFMerger(pdfs)

    def test_name_of_merge_pdf_if_no_filename_is_given(self):
        pdfs = ["example_file_1.pdf", "example_file_2.pdf"]
        merger = PDFMerger(pdfs)
        merger.merge_pdfs()
        assert "merged-file.pdf" in os.listdir()
        os.remove("merged-file.pdf")

    def test_name_of_merge_pdf_if_filename_is_given(self):
        pdfs = ["example_file_1.pdf", "example_file_2.pdf"]
        merger = PDFMerger(pdfs, "merged_example_file.pdf")
        merger.merge_pdfs()
        assert "merged_example_file.pdf" in os.listdir()
        os.remove("merged_example_file.pdf")

    def test_number_of_pages_for_the_merged_pdf(self):
        pdfs = ["example_file_1.pdf", "example_file_2.pdf"]
        merger = PDFMerger(pdfs, "merged_example_file.pdf")
        merger.merge_pdfs()
        file1_num_pages = PdfReader("example_file_1.pdf").get_num_pages()
        file2_num_pages = PdfReader("example_file_2.pdf").get_num_pages()
        merged_file_num_pages = PdfReader("merged_example_file.pdf").get_num_pages()
        assert file1_num_pages + file2_num_pages == merged_file_num_pages
        os.remove("merged_example_file.pdf")
