import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ], matches)
        
    def test_no_images(self):
        matches = extract_markdown_images("This is text with no images.")
        self.assertListEqual([], matches)
        
    def test_extract_single_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
        
    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )