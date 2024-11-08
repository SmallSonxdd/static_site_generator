from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType): 
        raise Exception("Text type of your Text node isn't valid type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        bold_text_html = LeafNode(tag='b', value=text_node.text)
        return bold_text_html
    if text_node.text_type == TextType.ITALIC:
        italic_text_html = LeafNode(tag='i', value=text_node.text) 
        return italic_text_html
    if text_node.text_type == TextType.CODE:
        code_text_html = LeafNode(tag='code', value=text_node.text)
        return code_text_html
    if text_node.text_type == TextType.LINK:
        link_text_html = LeafNode(tag='a', value=text_node.text, props={'href': f'{text_node.url}'}) 
        return link_text_html
    if text_node.text_type == TextType.IMAGE:
        image_text_html = LeafNode(tag='img', value='', props={'src': f'{text_node.url}', 'alt': f'{text_node.text}'})
        return image_text_html
    
    pass
