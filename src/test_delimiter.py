import unittest

from  split_delimiter import split_node_delimiter
from textnode import *

class test_split_delimiter(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("this is a **bold** message", text_type_text)
        test_split = split_node_delimiter(node,"**",text_type_bold)
        print(test_split)





