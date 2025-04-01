from textnode import TextNode, TextType
from source_to_dest import copy_dir
from generate_page import generate_page, clear_directory
from generate_pages_recursive import generate_pages_recursive

def main():
    clear_directory("./public")
    copy_dir("./static", "./public")
    generate_pages_recursive("./content/", "./template.html", "./public/")


main()