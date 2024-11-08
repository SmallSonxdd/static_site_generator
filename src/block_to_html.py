from text_to_html import *
from text_to_textnodes import *
from md_to_blocks import markdown_to_blocks
from block_type import block_to_block_type


def markdown_to_html_node(markdown):
    blocked_md = markdown_to_blocks(markdown)
    list_of_nodes = []
    for block in blocked_md:
        html_node = block_to_html_node(block)
        list_of_nodes.append(html_node)
    return ParentNode(tag='div', children=list_of_nodes)

#helper functions

def md_paragraph_to_text(block):
    lines = block.split('\n')
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)

def md_heading_to_text(block):
    type_of_heading = int(block_to_block_type(block)[1])
    final_text = block[type_of_heading+1:]
    children = text_to_children(final_text)
    return ParentNode(f"h{type_of_heading}", children)

def md_code_to_text(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode('code', children)
    return ParentNode('pre', [code])

def md_quote_to_text(block):
    list_of_lines = []
    lines = block.split('\n')
    for line in lines:
        list_of_lines.append(line[2:])
    content = ' '.join(list_of_lines)
    children = text_to_children(content)
    return ParentNode('blockquote', children)

def md_unordered_list_to_text(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))  
    return ParentNode('ul', html_items)
    
def md_ordered_list_to_text(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))  
    return ParentNode('ol', html_items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == 'PARAGRAPH':
        return md_paragraph_to_text(block)
    if block_type[0] == 'h' and block_type[1] in ['1', '2', '3', '4', '5', '6'] and len(block_type) == 2:
        return md_heading_to_text(block)
    if block_type == 'CODE':
        return md_code_to_text(block)
    if block_type == 'QUOTE':
        return md_quote_to_text(block)
    if block_type == 'UNORDERED LIST':
        return md_unordered_list_to_text(block)
    if block_type == 'ORDERED LIST':
        return md_ordered_list_to_text(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes