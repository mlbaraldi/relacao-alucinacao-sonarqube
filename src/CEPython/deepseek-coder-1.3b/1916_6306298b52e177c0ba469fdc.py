

def xml_children_as_dict(node):
    """
    Turn the children of node <xml> into a dict, keyed by tag name.

    This is only a shallow conversation - child nodes are not recursively processed.
    """
    children_dict = {}
    for child in node.childNodes:
        if child.nodeType == node.ELEMENT_NODE:
            children_dict[child.tagName] = child.childNodes
    return children_dict
