import unittest
import sys
sys.path.append('/home/admin1620/static_generator/src') 
from split_delimiter import *

class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):  
        node = TextNode("This is `code` here", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 3

        node = TextNode("Plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1

        node = TextNode("Hello `code` more `code`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 5

        node = TextNode("**bold text**", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1
        assert nodes[0].text_type == TextType.BOLD

        node = TextNode("This is `incomplete", TextType.TEXT)
        try:
            split_nodes_delimiter([node], "`", TextType.CODE)
            assert False, "Expected error for unclosed delimiter"
        except:
            assert True

if __name__ == "__main__":
    unittest.main()