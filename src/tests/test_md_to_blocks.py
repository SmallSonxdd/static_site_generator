import unittest

import sys
sys.path.append('/home/admin1620/static_generator/src') 
from md_to_blocks import *


class TestTextNode(unittest.TestCase):
    def test_provided_example(self):
        markdown = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        self.assertEqual(markdown_to_blocks(markdown), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])
    def test_empty_md(self):
        markdown = ''
        self.assertEqual(markdown_to_blocks(markdown), [])
    def test_just_whitespaces(self):
        markdown = ' \n\n    \n\t\n    \n\n\t\n\n\n     \t\n\t'
        self.assertEqual(markdown_to_blocks(markdown), []) 





if __name__ == "__main__":
    unittest.main()