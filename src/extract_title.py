from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            header = count_heading_level(block)
            return header
    raise Exception("No heading found in the markdown")

def count_heading_level(header_block):
    lines = header_block.strip().split('\n')
    if not lines:
        raise Exception("Header block is empty")

    first_line = lines[0].strip()

    level = 0
    for char in first_line:
        if char == '#':
            level += 1
        else:
            break

    if level > 0 and len(first_line) > level and first_line[level] != ' ':
         raise Exception("Invalid heading format: '#' must be followed by a space.")

    if level == 0:
        raise Exception("Not a heading block")
    elif level > 1:
        raise Exception(f"Heading level {level} is not Level 1.")
    elif level == 1:
        content = first_line.lstrip('#').strip()
        return content
    raise Exception("Unexpected state in count_heading_level")
