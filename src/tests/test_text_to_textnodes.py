import unittest

import sys
sys.path.append('/home/admin1620/static_generator/src') 
from text_to_textnodes import *


class TestTextNode(unittest.TestCase):
    def test_provided_example(self):
        nodes = text_to_textnodes('This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
        self.assertEqual(nodes, [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_empty_text(self):
        nodes = text_to_textnodes('')
        self.assertEqual(nodes, [])

    def test_plain_text(self):
        nodes = text_to_textnodes('Plain text')
        self.assertEqual(nodes, [TextNode('Plain text', TextType.TEXT)])

    def test_single_bold(self):
        nodes = text_to_textnodes('Just **bold** text')
        self.assertEqual(nodes, [TextNode('Just ', TextType.TEXT), TextNode('bold', TextType.BOLD), TextNode(' text', TextType.TEXT)])

    def test_multiple_italic(self):
        nodes = text_to_textnodes('*One* normal *two*')
        self.assertEqual(nodes, [TextNode('One', TextType.ITALIC), TextNode(' normal ', TextType.TEXT), TextNode('two', TextType.ITALIC)])

    def test_just_image(self):
        nodes = text_to_textnodes('![alternative text](http://www.linktoimage.com)')
        self.assertEqual(nodes, [TextNode('alternative text', TextType.IMAGE, 'http://www.linktoimage.com')])


    

    


if __name__ == "__main__":
    unittest.main()