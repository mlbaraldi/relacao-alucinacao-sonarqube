

def match_pubdate(node, pubdate_xpaths):
    """
    Returns the first match in the pubdate_xpaths list
    """
    for xpath in pubdate_xpaths:
        match = node.find(xpath)
        if match is not None:
            return match
    return None
