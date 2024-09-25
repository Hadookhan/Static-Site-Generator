import unittest

from htmlnode import ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    # WORKS
    def test_to_html(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
            "p"
        )

        html_node = node.to_html()
        # print(html_node)

        # WORKS
    def test_no_children(self):
        # node = ParentNode()

        # print(node)
        pass

    # WORKS
    def test_many_children(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
            "p"
        )

        html_node = node.to_html()
        # print(html_node)


