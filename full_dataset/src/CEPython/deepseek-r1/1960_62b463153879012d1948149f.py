def _eval_file(prefix, file_path):
    import os
    """
    Identifies the type of package file: `asset` or `rendition`.

    Determines the file type based on whether the filename (without extension)
    matches the given prefix and the file's extension. Updates the package
    information with the type and file path.

    Parameters
    ----------
    prefix : str
        The name of the XML file without its extension.
    file_path : str
        The full path to the file being evaluated.

    Returns
    -------
    dict
        A dictionary with keys 'type' (either 'asset' or 'rendition') and 'address' (the file path).
    """
    filename = os.path.basename(file_path)
    base, ext = os.path.splitext(filename)
    
    if base == prefix:
        if ext.lower() == '.xml':
            file_type = 'asset'
        else:
            file_type = 'rendition'
    else:
        file_type = 'asset'
    
    return {
        'type': file_type,
        'address': file_path
    }
