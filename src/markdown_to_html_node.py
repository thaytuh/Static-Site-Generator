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
            paragraph_node = paragraph_to_node(block)
            children.append(paragraph_node)
            
        elif block_type == BlockType.HEADING:
            heading_node = heading_to_node(block)
            children.append(heading_node)
        
        elif block_type == BlockType.CODE:
            pre_node = code_to_node(block)
            children.append(pre_node)
        
        elif block_type == BlockType.QUOTE:
            quote_node = quote_to_node(block)
            children.append(quote_node)
            
        elif block_type == BlockType.UNORDERED_LIST:
            unordered_list_node = unordered_list_to_node(block)
            children.append(unordered_list_node)
        
        elif block_type == BlockType.ORDERED_LIST:
            ordered_list_node = ordered_list_to_node(block)
            children.append(ordered_list_node)
        
    return ParentNode("div", children)



def text_to_children(text): # helper function - converts text to list of HTMLNodes
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

# helper functions - logic is stored in the below functions to make the primary function more readable

def paragraph_to_node(block): 
    clean_text = ' '.join(line.strip() for line in block.split('\n') if line.strip())
    paragraph_node = ParentNode("p", text_to_children(clean_text))
    return paragraph_node


def heading_to_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    level = min(max(level, 1), 6)
    
    content = block.lstrip('#').strip()
    heading_node = ParentNode(f"h{level}", text_to_children(content))
    return heading_node

def code_to_node(block):
    # special case - don't parse inline markdown
    lines = block.split('\n')
    start_index = 0
    end_index = len(lines)

    # Find first non-empty line index
    while start_index < len(lines) and not lines[start_index].strip():
        start_index += 1
    
    while end_index > start_index and not lines[end_index - 1].strip():
        end_index -= 1

    if start_index < end_index and lines[start_index].strip() == '```':
        start_index += 1
    
    if end_index > start_index and lines[end_index - 1].strip() == '```':
        end_index -= 1
        
    content_lines = lines[start_index:end_index]
    code_content = '\n'.join(content_lines)

    code_leaf_node = LeafNode("code", code_content)
    pre_node = ParentNode("pre", [code_leaf_node])
    return pre_node

def quote_to_node(block):
    lines = []
    for line in block.split('\n'):
        if line.startswith('>'):
            lines.append(line[1:].strip())
        else:
            lines.append(line.strip())
    content = ' '.join(lines)
    quote_node = ParentNode("blockquote", text_to_children(content))
    return quote_node

def unordered_list_to_node(block):
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
        
        list_item_node = ParentNode("li", text_to_children(item_text))
        list_items.append(list_item_node)

    unordered_list_node = ParentNode("ul", list_items)
    return unordered_list_node

def ordered_list_to_node(block):
    list_items = []
    for line in block.split('\n'):
        if not line.strip():
            continue
        
        item_text = line.strip()
        
        period_pos = item_text.find('.')
        if period_pos != -1:
            item_text = item_text[period_pos + 1:].strip()
        
        list_item_node = ParentNode("li", text_to_children(item_text))
        list_items.append(list_item_node)
    
    ordered_list_node = ParentNode("ol", list_items)
    return ordered_list_node