import unittest
from textnode import TextType, TextNode
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnode_full(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )
    
    def test_text_to_textnode_plain(self):
        text = "Just plain text without any markdown"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("Just plain text without any markdown", TextType.TEXT)],
            new_nodes
        )
        
    def test_text_to_textnode_bold_italic(self):
        text = "Text with **bold** and _italic_ formatting"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" formatting", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_text_to_textnode_code(self):
        text = "Here is `some code` in the middle of text"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("some code", TextType.CODE),
                TextNode(" in the middle of text", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_text_to_textnode_links(self):
        text = "Check out [my website](https://example.com) and [another site](https://test.org)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Check out ", TextType.TEXT),
                TextNode("my website", TextType.LINK, "https://example.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another site", TextType.LINK, "https://test.org"),
            ],
            new_nodes
        )
        
    def test_text_to_textnode_images(self):
        text = "Here's an ![example image](https://example.com/img.png) and another ![image](https://test.org/pic.jpg)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Here's an ", TextType.TEXT),
                TextNode("example image", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://test.org/pic.jpg"),
            ],
            new_nodes
        )

    def test_text_to_textnode_nested_formats(self):
        text = "Start **bold _italic_ text** and `code with **stars**`"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text_to_textnode_empty(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [],
            new_nodes
        )
    
    def test_text_to_textnode_incomplete_delimiters(self):
        text = "This has **only one star* and _single underscore"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text_to_textnode_consecutive_formats(self):
        text = "**Bold**_Italic_`Code`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Bold", TextType.BOLD),
                TextNode("Italic", TextType.ITALIC),
                TextNode("Code", TextType.CODE),
            ],
            new_nodes
        )

    def test_text_to_textnode_malformed_links_images(self):
        text = "Malformed [link](no url) and ![image]()"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Malformed ", TextType.TEXT),
                TextNode("link", TextType.LINK, "no url"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, ""),
            ],
            new_nodes
        )