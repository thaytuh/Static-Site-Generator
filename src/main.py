import sys
from textnode import TextNode, TextType
from source_to_dest import copy_dir
from generate_page import generate_page, clear_directory
from generate_pages_recursive import generate_pages_recursive

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
    

def main():
    clear_directory("./public")
    copy_dir("./static", "./public")
    generate_pages_recursive("./content/", "./template.html", "./public/", basepath)


    
main()