from textnode import TextType, TextNode
from extract_markdown import *

def split_nodes_image(old_nodes):
    result_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result_list.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            result_list.append(old_node)
            continue
        current_text = old_node.text
        for image in images:
            image_alt = image[0]
            image_link = image[1]
            sections = current_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections[0]) == 0:
                del sections[0]
            else:
                entry = result_list.append(TextNode(sections[0], TextType.TEXT))
                continue
            