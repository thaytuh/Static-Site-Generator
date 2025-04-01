from textnode import TextNode, TextType
from source_to_dest import copy_dir
from generate_page import generate_page, clear_directory

def main():
    clear_directory("./public")
    copy_dir("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()