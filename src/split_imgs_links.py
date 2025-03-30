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
            if sections[0]:
                result_list.append(TextNode(sections[0], TextType.TEXT))
            result_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
            
        if current_text:
            result_list.append(TextNode(current_text, TextType.TEXT))
            
    return result_list

def split_nodes_link(old_nodes):
    result_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result_list.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            result_list.append(old_node)
            continue
        current_text = old_node.text
        for link in links:
            link_text = link[0]
            link_url = link[1]
            sections = current_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0]:
                result_list.append(TextNode(sections[0], TextType.TEXT))
            result_list.append(TextNode(link_text, TextType.LINK, link_url))
            
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
            
        if current_text:
            result_list.append(TextNode(current_text, TextType.TEXT))
            
    return result_list