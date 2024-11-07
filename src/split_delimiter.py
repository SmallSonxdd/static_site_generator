from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(text_type, TextType):
        raise Exception('Invalid text_type')
    new_nodes = old_nodes.copy()    
    new_list = []

    for node in new_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
        else:
            helper_list = (node.text).split(delimiter)
            for index, item in enumerate(helper_list):
                if index % 2 == 0:
                    new_list.append(TextNode(item, TextType.TEXT))
                else:
                    new_list.append(TextNode(item, text_type))
    
    return new_list