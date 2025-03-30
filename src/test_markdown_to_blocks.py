import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_empty_string(self):
        # Test with an empty string
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_excessive_newlines(self):
        md = """First block


Second block



Third block"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block", "Third block"])
    
    def test_only_whitespace(self):
        md = """Real block



Another real block"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Real block", "Another real block"])
    
    def test_complex_blocks(self):
        md = """# Heading

Paragraph with **bold** and _italic_.

```
code block
with multiple
lines
```

- List item 1
- List item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Paragraph with **bold** and _italic_.",
                "```\ncode block\nwith multiple\nlines\n```",
                "- List item 1\n- List item 2"
            ]
        )
        
    def test_leading_trailing_newlines(self):
        md = """

First block

Last block

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Last block"])
    
    def test_single_block(self):
        md = "This is a single block with no newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block with no newlines"])