import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_default_init(self):
        node = HTMLNode()

        # Checks if each instance variable is None
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_node(self):
        node = HTMLNode("<h1>", "This is a html node", [], {"href": "https://www.google.com", "target": "_blank",})
        node_to_html = node.props_to_html()

        # Checks if return of props to html is string value and then ensures its not None
        self.assertIsInstance(node_to_html, str)
        self.assertIsNotNone(node_to_html)

    def test_repr(self):
        node = HTMLNode("<h1>", "This is a html node", [], {"href": "https://www.google.com", "target": "_blank",})
        
        #Ensures something is always output
        self.assertIsNotNone(node)


        