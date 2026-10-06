

def match_file_by_prefix(prefix, file_path):
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
    import os
    file_name = os.path.basename(file_path)
    return file_name.startswith(prefix)
