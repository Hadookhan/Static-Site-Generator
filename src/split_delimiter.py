from textnode import *

def split_node_delimiter(old_nodes, delimiter, text_type):
    match delimiter:
        case "**":
            text_type = text_type_bold
            return text_type
        case "*":
            text_type
    nodes_list = old_nodes.text.split()
    print(len(old_nodes.text))
    if delimiter not in old_nodes.text:
        raise Exception(f"There is no {delimiter} in this node")
    if old_nodes.text_type != text_type_text:
        raise Exception("node must be of a text type")
    char_in_nodes = []
    print(nodes_list)
    for node in nodes_list:
        if delimiter in node:
            return node
    print(node)
    return nodes_list

# split_node_delimiter(node, "*", text_type_bold)