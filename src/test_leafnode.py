import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_value_is_entered(self):
        node = LeafNode("This is a test message","p")
        node2 = LeafNode("This is a test message")

        self.assertIsNotNone(node.value)
        self.assertIsNotNone(node2.value)

    def test_to_html_method(self):
        node = LeafNode("This is a test message","a",{"href": "https://www.google.com"})
        node2 = LeafNode("This is a test message","p")
        node3 = LeafNode("This is a test message","p",234234)

        html_node = node.to_html()
        html_node2 = node2.to_html()
        html_node3 = node3.to_html()
        #print(html_node)    
        #print(html_node2)
        #print(html_node3)