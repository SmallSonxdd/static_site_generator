import unittest
import sys
sys.path.append('/home/admin1620/static_generator/src') 
from split_nodes import *

class TestTextNode(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("Look at this ![bootdev](https://www.boot.dev) picture!", TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("Look at this ", TextType.TEXT),
            TextNode("bootdev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" picture!", TextType.TEXT)
        ]

    def test_consecutive_images(self):
        node = TextNode("![image1](http://link1.com)![image2](http://link2.com)", TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("image1", TextType.IMAGE, "http://link1.com"),
            TextNode("image2", TextType.IMAGE, "http://link2.com")
        ]
    def test_no_images(self):
        node = TextNode("There's no picture here.", TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("There's no picture here.", TextType.TEXT)
        ]

    def test_mixed_content(self):
        node = TextNode("Start ![img1](link1) middle ![img2](link2) end.", TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("Start ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "link1"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "link2"),
            TextNode(" end.", TextType.TEXT)
        ]

    def test_same_image(self):
        node = TextNode("![bootdev](link1) regular text ![bootdev](link2)", TextType.TEXT,)
        result = split_nodes_image([node])
        assert result == [
            TextNode("bootdev", TextType.IMAGE, 'link1'),
            TextNode(" regular text ", TextType.TEXT),
            TextNode("bootdev", TextType.IMAGE, 'link2')
        ]

if __name__ == "__main__":
    unittest.main()