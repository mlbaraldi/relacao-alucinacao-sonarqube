def match_file_by_prefix(prefix, file_path):
    import os
    """
    Identify if a `file_path` belongs to a document package by a given `prefix`

    Returns `True` for documents belonging to a package.

    Parameters
    ----------
    prefix : str
        Filename prefix
    file_path : str
        File path
    Returns
    -------
    bool
        True - file belongs to the package
    """
    filename = os.path.basename(file_path)
    return filename.startswith(prefix)
