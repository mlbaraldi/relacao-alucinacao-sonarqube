

def strip_root(path, root):
    """
    Remove root from path, throw exception on failure.
    """
    try:
        if path.startswith(root):
            return path[len(root):]
        else:
            raise ValueError("Path does not start with root")
    except Exception as e:
        raise ValueError("Failed to strip root from path") from e
