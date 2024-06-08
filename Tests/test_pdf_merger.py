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
        base_dir = os.path.dirname(__file__)
        pdfs = [os.path.join(base_dir, "example_file_1.pdf"), os.path.join(base_dir, "example_file_2.pdf")]
        merger = PDFMerger(pdfs)
        output_file = os.path.join(base_dir, "merged_file.pdf")
        merger.merge_pdfs()
        assert os.path.isfile(output_file)
        os.remove(output_file)
        
    def test_name_of_merge_pdf_if_filename_is_given(self):
        base_dir = os.path.dirname(__file__)
        pdfs = [os.path.join(base_dir, "example_file_1.pdf"), os.path.join(base_dir, "example_file_2.pdf")]
        merger = PDFMerger(pdfs)
        output_file = os.path.join(base_dir, "merged_example_file.pdf")
        merger.merge_pdfs(output_file)
        assert os.path.isfile(output_file)
        os.remove(output_file)

    def test_number_of_pages_for_the_merged_pdf(self):
        base_dir = os.path.dirname(__file__)
        pdfs = [os.path.join(base_dir, "example_file_1.pdf"), os.path.join(base_dir, "example_file_2.pdf")]
        merger = PDFMerger(pdfs)
        output_file = os.path.join(base_dir, "merged_new_example_file.pdf")
        merger.merge_pdfs(output_file)
        file1_num_pages = PdfReader(pdfs[0]).get_num_pages()
        file2_num_pages = PdfReader(pdfs[1]).get_num_pages()
        merged_file_num_pages = PdfReader(output_file).get_num_pages()
        assert file1_num_pages + file2_num_pages == merged_file_num_pages
        os.remove(output_file)
