import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_headings(self):
        self.assertEqual(block_to_block_type("# Level 1 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Level 2 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Level 3 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Level 4 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Level 5 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Level 6 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### Too many hashtags"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#No space after hashtag"), BlockType.PARAGRAPH)
    
    def test_code_blocks(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\nmulti-line\ncode block\n```"), BlockType.CODE)
        # edge cases
        self.assertEqual(block_to_block_type("```\nincomplete code block"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("``not enough backticks``"), BlockType.PARAGRAPH)
    
    def test_quotes(self):
        self.assertEqual(block_to_block_type(">Single line quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">Line 1\n>Line 2"), BlockType.QUOTE)
        # edge cases
        self.assertEqual(block_to_block_type(">Line 1\nLine 2 without >"), BlockType.PARAGRAPH)
        
    def test_unordered_lists(self):
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
        # edge cases
        self.assertEqual(block_to_block_type("- Item 1\nNot an item"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("-No space after dash"), BlockType.PARAGRAPH)
        
    def test_ordered_lists(self):
        self.assertEqual(block_to_block_type("1. Item 1"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ORDERED_LIST)
        # edge cases
        self.assertEqual(block_to_block_type("1. Item 1\n3. Skipped number"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1.No space after period"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("2. Starting with wrong number\n3. Still wrong number"), BlockType.PARAGRAPH)
    
    def test_paragraphs(self):
        self.assertEqual(block_to_block_type("Plain text paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Multi-line\nparagrah"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Text with # but not at start"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Text with > but not at start \neach line"), BlockType.PARAGRAPH)