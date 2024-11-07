from textnode import TextType, TextNode
from extract_md import *

def split_nodes_image(old_nodes):
    new_nodes = old_nodes.copy()
    new_list = []
    for node in new_nodes:
        exctracted = extract_markdown_images(node.text)
        if exctracted == []:
            if node.text != '':
                new_list.append(node)
        else:
            list_of_tuples_of_images = exctracted
            list_of_image_splitters = []
            for alt_text, url in list_of_tuples_of_images:
                list_of_image_splitters.append(f'![{alt_text}]({url})')
            index = 0
            index_of_tuple_list = 0
            for splitter in list_of_image_splitters:
                start_index = node.text.find(splitter, index)

                if index < start_index:
                    text_before = node.text[index:start_index]
                    new_list.append(TextNode(text_before, TextType.TEXT))
                
                new_list.append(TextNode(list_of_tuples_of_images[index_of_tuple_list][0], TextType.IMAGE, list_of_tuples_of_images[index_of_tuple_list][1]))

                index = start_index + len(splitter)
                index_of_tuple_list += 1

            if index < len(node.text):
                remaining_text = node.text[index:]
                new_list.append(TextNode(remaining_text, TextType.TEXT))

    return new_list



def split_nodes_link(old_nodes):
    new_nodes = old_nodes.copy()
    new_list = []
    for node in new_nodes:
        exctracted = extract_markdown_links(node.text)
        if exctracted == []:
            if node.text != '':
                new_list.append(node)
        else:
            list_of_tuples_of_images = exctracted
            list_of_image_splitters = []
            for alt_text, url in list_of_tuples_of_images:
                list_of_image_splitters.append(f'[{alt_text}]({url})')
            index = 0
            index_of_tuple_list = 0
            for splitter in list_of_image_splitters:
                start_index = node.text.find(splitter, index)

                if index < start_index:
                    text_before = node.text[index:start_index]
                    new_list.append(TextNode(text_before, TextType.TEXT))
                
                new_list.append(TextNode(list_of_tuples_of_images[index_of_tuple_list][0], TextType.LINK, list_of_tuples_of_images[index_of_tuple_list][1]))

                index = start_index + len(splitter)
                index_of_tuple_list += 1

            if index < len(node.text):
                remaining_text = node.text[index:]
                new_list.append(TextNode(remaining_text, TextType.TEXT))

    return new_list
