from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # heading
    if block.startswith("#"):
        parts = block.split(' ', 1)
        if len(parts) > 1 and all(char == '#' for char in parts[0]) and 1 <= len(parts[0]) <= 6:
            return BlockType.HEADING
    # code
    elif block.strip().startswith("```") and block.strip().endswith("```"):
        return BlockType.CODE
    # quote
    elif all(line.startswith(">") for line in block.split('\n') if line.strip()):
        return BlockType.QUOTE
    # unordered list
    elif all(line.startswith("- ") for line in block.split('\n') if line.strip()):
        return BlockType.UNORDERED_LIST
    # ordered list
    elif all(line.strip() for line in block.split('\n')):
        lines = [line for line in block.split('\n') if line.strip()]
        valid_ordered_list = True
        
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                valid_ordered_list = False
                break
        if valid_ordered_list:
            return BlockType.ORDERED_LIST
    # default to paragraph
    return BlockType.PARAGRAPH