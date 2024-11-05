import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_but_url(self):
        node = TextNode('Sample text', TextType.ITALIC, url='smegma')
        node2 = TextNode('Sample text', TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_different_type(self):
        node = TextNode('Sample text', TextType.ITALIC)
        node2 = TextNode('Sample text', TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_different_text(self):
        node = TextNode('Sample', TextType.ITALIC, url='http://www.google.com/')
        node2 = TextNode('Sample text', TextType.ITALIC, url='http://www.google.com/')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
