

def select_filenames_by_prefix(prefix, files):
    """
    Get files which belongs to a document package.

    Returns files from the list `files` whose names start with `prefix`

    Parameters
    ----------
    prefix : str
        Filename prefix
    files : str list
        Files paths

    Returns
    -------
    list
        Files paths which basename files matches to prefix
    """
    return [file for file in files if file.startswith(prefix)]
