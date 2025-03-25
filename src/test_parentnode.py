import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_node_with_multiple_children(self):
        child1 = LeafNode("span", "first")
        child2 = LeafNode("span", "second")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), "<div><span>first</span><span>second</span></div>")

    def test_parent_node_with_mixed_leaf_and_parent_children(self):
        leaf_child = LeafNode("b", "bold")
        parent_child = ParentNode("p", [LeafNode("i", "italic")])
        parent = ParentNode("div", [leaf_child, parent_child])
        self.assertEqual(parent.to_html(), "<div><b>bold</b><p><i>italic</i></p></div>")

    def test_parent_node_with_properties(self):
        child = LeafNode("span", "content")
        parent = ParentNode("div", [child], {"class": "container", "id": "main"})
        self.assertEqual(parent.to_html(), '<div class="container" id="main"><span>content</span></div>')

    def test_parent_node_with_none_tag(self):
        child = LeafNode("span", "content")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_node_with_empty_children_list(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_parent_node_with_none_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()