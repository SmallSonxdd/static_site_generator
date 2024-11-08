from text_to_html import *
from text_to_textnodes import *
from md_to_blocks import markdown_to_blocks
from block_type import block_to_block_type


def markdown_to_html_node(markdown):
    blocked_md = markdown_to_blocks(markdown)
    list_of_nodes = []
    for block in blocked_md:
        block_type = block_to_block_type(block)
        node = ParentNode(tag=f'{block_type_to_tag(block_type)}', children=text_to_children(block, block_type))
        list_of_nodes.append(node)

    return ParentNode(tag='div', children=list_of_nodes)

#helper functions

def md_heading_to_text(text):
    type_of_heading = int(block_to_block_type(text)[1])
    final_text = text[type_of_heading+1:]
    return final_text

def md_code_to_text(text):
    final_text = text[3:-3]
    return final_text

def md_quote_to_text(text):
    list_of_lines = []
    lines = text.split('\n')
    for line in lines:
        list_of_lines.append(line[2:])
    final_text = '\n'.join(list_of_lines)
    return final_text

def md_unordered_list_to_text(text):
    list_of_lines = []
    lines = text.split('\n')
    for line in lines:
        list_of_lines.append(line[2:])
    final_text = '!'.join(list_of_lines)
    return final_text
    
def md_ordered_list_to_text(text):
    list_of_lines = []
    lines = text.split('\n')
    for line in lines:
        list_of_lines.append(line[3:])
    final_text = '\n'.join(list_of_lines)
    return final_text   

def text_to_children(text, block_type):
    string_of_text = text
    if block_type[0] == 'h':
        string_of_text = md_heading_to_text(text)
    if block_type == 'CODE':
        string_of_text = md_code_to_text(text)
    if block_type == 'QUOTE':
        string_of_text = md_quote_to_text(text)
    if block_type in ["UNORDERED LIST", "ORDERED LIST"]:
        lines = text.split('\n')
        list_items = []
        for line in lines:
            if block_type == 'UNORDERED LIST':
                line = line[2:]
            else:
                line = line[3:]
            text_nodes = text_to_textnodes(line)
            html_nodes = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                html_nodes.append(html_node)
            list_items.append(ParentNode(tag="li", children=html_nodes))
        return list_items
    text_nodes = text_to_textnodes(string_of_text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def text_to_html_nodes(list_of_text):
    pass

def block_type_to_tag(block_type):
    if block_type == 'PARAGRAPH':
        return 'p'    
    if block_type[0] == 'h':
        return f'h{block_type[1]}'
    if block_type == 'CODE':
        return 'code'
    if block_type == 'QUOTE':
        return 'blockquote'
    if block_type == 'UNORDERED LIST':
        return 'ul'
    if block_type == 'ORDERED LIST':
        return 'ol'






md = '### This is a heading\n\nThis is a ```paragraph``` of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
print(markdown_to_html_node(md))