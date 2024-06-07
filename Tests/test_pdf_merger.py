'''
Tests for the pdf_merger script
'''

import unittest
from pdf_merger import PDFMerger

class TestPDFMerger(unittest.TestCase):
    def test_valueerror_is_raised_if_number_of_pdfs_is_zero(self):
        pass

    def test_valueerror_is_raised_if_number_of_pdfs_is_one(self):
        pass

    def test_name_of_merge_pdf_if_no_filename_is_given(self):
        pass

    def test_name_of_merge_pdf_if_filename_is_given(self):
        pass

    def test_number_of_pages_for_the_merged_pdf(self):
        pass

    # A thought I had:
    # Put merge pdfs in another folder to avoid overwriting files!
