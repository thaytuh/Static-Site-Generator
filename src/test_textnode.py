import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a another text node", TextType.ITALIC)
        node4 = TextNode("This is a URL text node", TextType.LINK)
        self.assertEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()