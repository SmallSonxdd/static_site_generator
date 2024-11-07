import unittest
import sys
sys.path.append('/home/admin1620/static_generator/src') 
from extract_md import *


class TestTextNode(unittest.TestCase):
    def test_single_image(self):
        text = "This is text with a single image ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    
    def test_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_with_no_images(self):
        text = "This is random text without any images, let's see"
        self.assertEqual(extract_markdown_images(text), [])

    def test_malfored_image(self):
        text = "This is text with a single image ![rick roll] (https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [])
    
    def test_extract_image_with_link_input(self):
        text = 'Some text with a link instead of image [this is a link, not an image](https://www.youtube.com/watch?v=cdGLKoIZPNs)'
        self.assertEqual(extract_markdown_images(text), [])
    


if __name__ == '__main__':
    unittest.main()