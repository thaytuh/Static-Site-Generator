from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []
    for node in old_nodes:
        # if node is not a TEXT node, just add to results unchanged
        if node.text_type is not TextType.TEXT:
            result_list.append(node)
        else:
            # for TEXT nodes we need to process the text content
            text = node.text
            # process the text and add resulting nodes to result_list
            process_text(text, delimiter, text_type, result_list)
    return result_list

def process_text(text, delimiter, text_type, result_list):
    remaining_text = text
    
    while delimiter in remaining_text:
        start = remaining_text.find(delimiter)
        end = remaining_text.find(delimiter, start + len(delimiter))
        
        if end == -1:
            raise ValueError(f"No closing delimiter for {delimiter}")
        
        # text before first delimiter
        before = remaining_text[:start]
        # text between delimiters (not including delimiters themselves)
        between = remaining_text[start + len(delimiter):end]
        # text after second delimiter
        after = remaining_text[end + len(delimiter):]
        
        # add nodes for the three sections
        if before:
            result_list.append(TextNode(before, TextType.TEXT))
        if between:
            result_list.append(TextNode(between, text_type))
        
        # update remaining_text to continue processing
        remaining_text = after
        
    # append remaining text after all delimiters are processed
    if remaining_text:
        result_list.append(TextNode(remaining_text, TextType.TEXT))