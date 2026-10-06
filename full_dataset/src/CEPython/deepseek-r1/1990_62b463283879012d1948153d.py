def match_pubdate(node, pubdate_xpaths):
    """
    Returns the first match in the pubdate_xpaths list
    """
    for xpath in pubdate_xpaths:
        results = node.xpath(xpath)
        if results:
            return results[0]
    return None
