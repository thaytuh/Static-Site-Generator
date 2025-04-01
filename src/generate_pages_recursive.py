import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)

    for dirpath, _, filenames in os.walk(dir_path_content):
        for filename in filenames:
            if filename.endswith(".md"):
                source_md_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(dirpath, dir_path_content)
                if relative_path == '.':
                    dest_subdir_path = dest_dir_path
                else:
                    dest_subdir_path = os.path.join(dest_dir_path, relative_path)

                os.makedirs(dest_subdir_path, exist_ok=True)

                dest_html_filename = filename[:-3] + ".html"
                dest_html_path = os.path.join(dest_subdir_path, dest_html_filename)

                generate_page(source_md_path, template_path, dest_html_path, basepath)
    