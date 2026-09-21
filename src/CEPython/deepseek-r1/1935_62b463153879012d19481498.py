def files_list(path):
    import os
    """
    Return the files in `path`
    """
    return [entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))]
