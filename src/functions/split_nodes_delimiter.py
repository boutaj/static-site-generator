import re

from nodes.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    the_splited_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            the_splited_nodes.append(old_node)
        else:
            # Make sure it have it closing delimiter (should be even)
            if old_node.text.count(delimiter) % 2 != 0:
                raise Exception("The delimiters didn't match!")
            new_nodes = re.split(rf'({re.escape(delimiter)})', old_node.text)
            is_del = False
            for node in new_nodes: 
                if node == delimiter:
                    is_del = not is_del
                    continue
                if node:
                    the_splited_nodes.append(TextNode(node, text_type if is_del else TextType.TEXT))
    return the_splited_nodes

