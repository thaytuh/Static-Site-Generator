import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        # Create a node with an href property
        node = HTMLNode(props={"href": "https://www.example.com"})
        # Test that props_to_html returns the expected string
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')
    
    def test_props_to_html_with_no_props(self):
        # Test when props is an empty dictionary
        node = HTMLNode(props={})
        # Should return an empty string
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        # Should include both properties with spaces before each
        # Note: order might vary, so you may need to check for both possibilities
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_none_props(self):
        # Test when props is None (default)
        node = HTMLNode()
        # Should return an empty string
        self.assertEqual(node.props_to_html(), "")
    
if __name__ == "__main__":
    unittest.main()