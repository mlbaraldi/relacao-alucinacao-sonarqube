

def strip_root(path, root):
    """
    Remove root from path, throw exception on failure.
    """
    if not path.startswith(root):
        raise ValueError("Path does not start with root")
    return path[len(root):]
