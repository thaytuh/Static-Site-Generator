import unittest
from textnode import TextNode, TextType
from split_imgs_links import split_nodes_image, split_nodes_link

class TestSplitImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_no_image(self):
        node = TextNode(
            "This is text without an image",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],
            new_nodes
        )
    
    def test_non_text_node_image(self):
        node = TextNode("Some bold text", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_multiple_nodes_link(self):
        node1 = TextNode("Text with [link](https://example.com)", TextType.TEXT)
        node2 = TextNode("Text without link", TextType.TEXT)
        new_nodes = split_nodes_link([node1, node2])
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            node2
        ]
        self.assertListEqual(expected, new_nodes)
    
    def test_image_at_beginning(self):
        node = TextNode("![first](https://example.com/img.jpg) then text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/img.jpg"),
                TextNode(" then text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_link_at_end(self):
        node = TextNode("Text and then [link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text and then ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com")
            ],
            new_nodes
        )
    
    def test_consecutive_images(self):
        node = TextNode("![img1](https://example.com/1.jpg)![img2](https://example.com/2.jpg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "https://example.com/1.jpg"),
                TextNode("img2", TextType.IMAGE, "https://example.com/2.jpg")
            ],
            new_nodes
        )
        
    def test_empty_text_between_links(self):
        node = TextNode("[link1](https://example.com/1)[link2](https://example.com/2)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "https://example.com/1"),
                TextNode("link2", TextType.LINK, "https://example.com/2")
            ],
            new_nodes
        )

    def test_empty_text_between_images(self):
        node = TextNode("![img1](https://example.com/1.jpg)![img2](https://example.com/2.jpg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "https://example.com/1.jpg"),
                TextNode("img2", TextType.IMAGE, "https://example.com/2.jpg")
            ],
            new_nodes
        )