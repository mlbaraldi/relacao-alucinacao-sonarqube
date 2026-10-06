

def strip_root(path, root):
    if not path.startswith(root):
        raise ValueError("Path does not start with root")
    return path[len(root):]
