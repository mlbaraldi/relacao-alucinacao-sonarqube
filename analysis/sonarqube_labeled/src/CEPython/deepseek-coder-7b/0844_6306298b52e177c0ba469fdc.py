import xml.etree.ElementTree as ET


def xml_children_as_dict(node):
    """
    Turn the children of node <xml> into a dict, keyed by tag name.

    This is only a shallow conversation - child nodes are not recursively processed.
    """
    children_dict = {}
    for child in node:
        if child.tag not in children_dict:
            children_dict[child.tag] = []
        children_dict[child.tag].append(child)
    return children_dict
