import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )


    def test_heading(self):
        md = """
# This is a main heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a main heading</h1></div>"
        )


    def test_quote(self):
        md = """
> This is an
> example of
> a quote block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is an example of a quote block</blockquote></div>"
        )


    def test_unordered_list(self):
        md = """
- This is an
- example of
- an unordered list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an</li><li>example of</li><li>an unordered list</li></ul></div>"
        )


    def test_ordered_list(self):
        md = """
1. This is an
2. example of
3. an ordered list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an</li><li>example of</li><li>an ordered list</li></ol></div>"
        )

   
    def test_mixed_formatting(self):
        md = """
This is mixed formatting with **bold**, _italic_, and `inline code`.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is mixed formatting with <b>bold</b>, <i>italic</i>, and <code>inline code</code>.</p></div>"
        )


    def test_empty_input(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")


    def test_incomplete_markdown(self):
        md = """
This is **bold but not closed and _italic but also not closed.
"""
        with self.assertRaises(ValueError):
            node = markdown_to_html_node(md)
            node.to_html()


    def test_newline_between_blocks(self):
        md = """
### A heading

This should be a paragraph right after the heading.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>A heading</h3><p>This should be a paragraph right after the heading.</p></div>")
    
    def test_multiple_paragraphs(self):
        md = """
This is the first paragraph.

This is the second paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is the first paragraph.</p><p>This is the second paragraph.</p></div>"
        )
    
    def test_mixed_headings(self):
        md = """
# Heading 1

Some paragraph under heading 1.

## Heading 2

Another paragraph under heading 2.

### Heading 3

And even deeper!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p>Some paragraph under heading 1.</p><h2>Heading 2</h2><p>Another paragraph under heading 2.</p><h3>Heading 3</h3><p>And even deeper!</p></div>"
        )
    
    def test_list_blocks(self):
        md = """
- Item 1
- Item 2
- Item 3

1. First ordered item
2. Second ordered item

Third-level paragraph after lists.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><ol><li>First ordered item</li><li>Second ordered item</li></ol><p>Third-level paragraph after lists.</p></div>"
        )
    
    def test_code_block(self):
        md = """
```
def example():
# This is an inline comment
return "**This should not be bold**"
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def example():\n# This is an inline comment\nreturn \"**This should not be bold**\"</code></pre></div>"
        )
    
    def test_nested_in_blockquote(self):
        md = """
> This is a **bold** blockquote with:
> - A list item
> - Another list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <b>bold</b> blockquote with: - A list item - Another list item</blockquote></div>"
        )
    
    def test_multiple_empty_lines(self):
        md = """
This is the first paragraph.


This is the second paragraph with extra empty space between blocks.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is the first paragraph.</p><p>This is the second paragraph with extra empty space between blocks.</p></div>"
        )
    
    def test_formatted_list_items(self):
        md = """
- This is a **bold** item
- This contains _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a <b>bold</b> item</li><li>This contains <i>italic</i> text</li></ul></div>"
        )
    
    def test_links(self):
        md = """
This is a link to [Boot.dev](https://boot.dev).
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a link to <a href=\"https://boot.dev\">Boot.dev</a>.</p></div>"
        )
    
    def test_special_characters(self):
        md = """
This <text> & that > text with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This <text> & that > text with <b>bold</b></p></div>"
        )