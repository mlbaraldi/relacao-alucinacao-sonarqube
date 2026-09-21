

def strip_root(path, root):
    """
    Remove root from path, throw exception on failure.
    """
    if not path.startswith(root):
        raise ValueError(f"Path {path} does not start with root {root}")
    return path[len(root):]
