from split_delimiter import *
from split_nodes import *

def text_to_textnodes(text_input):
    new_text_node = TextNode(text_input, TextType.TEXT)
    # link delimiter
    unlinked_text_nodes = split_nodes_link([new_text_node])    
    # bold delimiter
    unbolded_text_nodes = split_nodes_delimiter(unlinked_text_nodes, '**', TextType.BOLD)
    # italic delimiter
    unitaliced_text_nodes = split_nodes_delimiter(unbolded_text_nodes, '*', TextType.ITALIC)
    # code delimiter
    codeless_text_nodes = split_nodes_delimiter(unitaliced_text_nodes, '`', TextType.CODE)
    # image delimiter
    unimaged_text_nodes = split_nodes_image(codeless_text_nodes)

    return unimaged_text_nodes



