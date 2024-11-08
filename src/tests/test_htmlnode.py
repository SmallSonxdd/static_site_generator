import unittest

import sys
sys.path.append('/home/admin1620/static_generator/src') 
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag='<a>', 
        value='Sample text', 
        children=['idk', 'what', 'children', 'are'], 
        props={"href": "https://www.google.com", "target": "_blank",}
        )
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node2 = HTMLNode(props={'kungen': 'slungen'})
        self.assertEqual(node2.props_to_html(), ' kungen="slungen"')

        node3 = HTMLNode()
        self.assertEqual(node3.props_to_html(), '')

    def test_repr(self):
        node1 = HTMLNode(tag='<a>', 
        value='Sample text', 
        children=['idk', 'what', 'children', 'are'], 
        props={"href": "https://www.google.com", "target": "_blank",}
        )
        result = node1.__repr__()
        self.assertIn('a>', result)
        self.assertIn('children', result)
        self.assertIn('[', result)
        self.assertIn('text', result)
        self.assertNotIn('$', result)


    
    
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    # from here it's leaf tests

    def test_to_html_leaf(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), '<p>This is a paragraph of text.</p>')

        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        leaf3 = LeafNode(tag=None, value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(leaf3.to_html(), 'Click me!')

    def test_parent_node_is_eq(self):
        parent_node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(parent_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parent_node_nested_with_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
            'p',
            [
                LeafNode("b", "young"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
        
            ], {"href": "https://www.google.com", "$$$$$": "#####"}
        )
        
            ], 
        )

        self.assertEqual(parent_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p href="https://www.google.com" $$$$$="#####"><b>young</b>Normal text<i>italic text</i>Normal text</p></p>')
    
if __name__ == "__main__":
    unittest.main()
