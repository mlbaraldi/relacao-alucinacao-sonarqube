import xml.etree.ElementTree as ET


def xml_children_as_dict(node):
    """
    Turn the children of node <xml> into a dict, keyed by tag name.

    This is only a shallow conversation - child nodes are not recursively processed.
    """
    # Parse the XML node
    xml_node = ET.fromstring(node)

    # Create a dictionary with tag names as keys and child nodes as values
    children_dict = {child.tag: child for child in xml_node}

    return children_dict
