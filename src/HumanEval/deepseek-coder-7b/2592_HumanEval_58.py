

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    return sorted(list(set(l1) & set(l2)))

