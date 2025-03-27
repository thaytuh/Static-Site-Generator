import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_single_delimiter_pair(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_delimiter_pairs(self):
        node = TextNode("Text with `code` and more `code blocks`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " and more ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        
    def test_missing_closing_delimiter(self):
        node = TextNode("Text with `unclosed code", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_nodes_preserved(self):
        nodes = [
            TextNode("Regular text", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More regular `with code`", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Regular text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Already bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, "More regular ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "with code")
        self.assertEqual(result[3].text_type, TextType.CODE)

    def test_different_delimiters(self):
        # Test with bold delimiters
        node = TextNode("Text with **bold words** in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "bold words")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        
        # Test with italic delimiters
        node = TextNode("Text with _italic words_ in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "italic words")