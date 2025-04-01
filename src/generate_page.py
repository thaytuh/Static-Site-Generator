import os, shutil
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    markdown_file = get_file_from_source_path(from_path)
    template_file = get_file_from_source_path(template_path)
    markdown_as_html = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    index_with_title = template_file.replace("{{ Title }}", title)
    final_index_html = index_with_title.replace("{{ Content }}", markdown_as_html)
    final_index_html = final_index_html.replace('href="/', f'href="{basepath}')
    final_index_html = final_index_html.replace('src="/', f'src="{basepath}')
    create_directory(dest_path)
    create_html_file(dest_path, final_index_html)


def get_file_from_source_path(from_path):
    try:
        with open(from_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Error: File not found")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None


def create_directory(destination_path):
    dir_name = os.path.dirname(destination_path)
    os.makedirs(dir_name, exist_ok=True)

def create_html_file(destination_path, content):
    try:
        with open(destination_path, 'w') as html_file:
            html_file.write(content)
        return True
    except Exception as e:
        print(f"Error creating HTML file: {e}")
        return False



def clear_directory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

