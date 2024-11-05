import unittest
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_html import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_link_check(self):
        tnode = TextNode("link", TextType.LINK, url="https://www.google.com")
        hnode = text_node_to_html_node(tnode)
        target_html = '<a href="https://www.google.com">link</a>'
        self.assertEqual(hnode, target_html)
        

if __name__ == "__main__":
    unittest.main()
