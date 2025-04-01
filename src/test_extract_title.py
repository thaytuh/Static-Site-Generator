import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_heading(self):
        md = """
        # This is a heading"""
        
        heading = extract_title(md)
        self.assertEqual(
            heading,
            "This is a heading"
        )
    
    def test_multiple_headings(self):
        md = """
        # This is the main heading
        
        ## This is a subheading"""
        
        heading = extract_title(md)
        self.assertEqual(
            heading,
            "This is the main heading"
        )
    
    def test_no_h1_heading(self):
        md = """
        ## This is a level 2 heading
        
        This is a paragraph"""
        
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_no_space(self):
        md = """
        #This is a heading with no space after the #"""
        
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_no_heading(self):
        md = """
        This is a block with no heading"""
        
        with self.assertRaises(Exception):
            extract_title(md)
        
    def test_empty_header(self):
        md = """
        # """
        
        with self.assertRaises(Exception):
            extract_title(md)
            
    def test_empty_md(self):
        md = """"""
        
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_h1_after_h2(self):
        md = """
        ## This is an h2 heading
        
        # This is an h1 heading"""
        
        with self.assertRaises(Exception):
            extract_title(md)