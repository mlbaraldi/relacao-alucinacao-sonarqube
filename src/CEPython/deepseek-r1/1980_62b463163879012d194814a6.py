def files_list_from_zipfile(zip_path):
    import zipfile
    """
    Return the files in `zip_path` as a list of strings.
    """
    with zipfile.ZipFile(zip_path, 'r') as zf:
        return zf.namelist()
