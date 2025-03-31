from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown): # primary function
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            paragraph_node = ParentNode("p", text_to_children(block))
            children.append(paragraph_node)
            
        elif block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            level = min(max(level, 1), 6)
            
            content = block.lstrip('#').strip()
            heading_node = ParentNode(f"h{level}", text_to_children(content))
            children.append(heading_node)
        
        elif block_type == BlockType.CODE:
            # special case - don't parse inline markdown
            code_content = block.strip('`').strip()
            code_text_node = TextNode(code_content, TextType.TEXT)
            code_html_node = text_node_to_html_node(code_text_node)
            pre_node = ParentNode("pre", [ParentNode("code", [code_html_node])])
            children.append(pre_node)
        
        elif block_type == BlockType.QUOTE:
            content = block.strip('>').strip()
            quote_node = ParentNode("blockquote", text_to_children(content))
            children.append(quote_node)
            
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in block.split('\n'):
                # skips empty lines
                if not line.strip():
                    continue
                # remove the '- ' at the start and process the rest
                item_text = line.strip()
                if item_text.startswith("- "):
                    item_text = item_text[2:].strip()
                elif item_text.startswith("-"):
                    item_text = item_text[1:].strip()
                
                item_children = text_to_children(item_text)
                list_item_node = ParentNode("li", item_children)
                list_items.append(list_item_node)

            unordered_list_node = ParentNode("ul", list_items)
            children.append(unordered_list_node)
        
        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            for line in block.split('\n'):
                if not line.strip():
                    continue
                
                item_text = line.strip()
                
                period_pos = item_text.find('.')
                if period_pos != -1:
                    item_text = item_text[period_pos + 1:].strip()
                
                item_children = text_to_children(item_text)
                list_item_node = ParentNode("li", item_children)
                list_items.append(list_item_node)
            
            ordered_list_node = ParentNode("ol", list_items)
            children.append(ordered_list_node)
        
    return ParentNode("div", children)

def text_to_children(text): # helper function - 
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes