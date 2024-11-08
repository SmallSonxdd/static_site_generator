from block_to_html import *
import os
import shutil

def extract_title(markdown):
    list_of_md_lines = markdown.split('\n\n')
    for line in list_of_md_lines:
        if line.startswith('# '):
            text = line[2:]
            return text.strip()
    raise Exception('no h1 markdown block')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    title = extract_title(markdown_content)
    html_string = (markdown_to_html_node(markdown_content)).to_html()
    html_page = (template_content.replace('{{ Title }}', title)).replace('{{ Content }}', html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for item in contents:
        full_path = os.path.join(dir_path_content, item)
        relative_path = os.path.relpath(full_path, dir_path_content)
        if os.path.isfile(full_path):
            if item[-3:] == '.md':
                os.makedirs(os.path.join(dest_dir_path, os.path.dirname(relative_path)), exist_ok=True)
                dest_file = relative_path[:-3] + '.html'
                full_dest_path = os.path.join(dest_dir_path, dest_file)
                generate_page(full_path, template_path, full_dest_path)
        else:
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, item))

def source_to_destination(source_directory, destination_directory):
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
    os.makedirs(destination_directory, exist_ok=True)
    contents = os.listdir(source_directory)
    for item in contents:
        source_path = os.path.join(source_directory, item)
        destination_path = os.path.join(destination_directory, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            source_to_destination(source_path, destination_path)
    return destination_directory