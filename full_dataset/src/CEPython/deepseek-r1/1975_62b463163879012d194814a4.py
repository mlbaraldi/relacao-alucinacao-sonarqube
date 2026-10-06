def _explore_zipfile(zip_path):
    import os
    import zipfile
    """
    Get packages' data from zip_path by grouping files by their XML basename.

    Parameters
    ----------
    zip_path : str
        zip file path

    Returns
    -------
    dict
        A dictionary where keys are XML basenames and values are lists of files sharing that basename.
    """
    groups = {}
    xml_basenames = set()

    with zipfile.ZipFile(zip_path, 'r') as zf:
        # First pass: collect all XML file basenames
        for name in zf.namelist():
            if name.endswith('/'):
                continue  # Skip directories
            if name.lower().endswith('.xml'):
                basename = os.path.splitext(name)[0]
                xml_basenames.add(basename)

        # Second pass: group files by XML basenames
        for name in zf.namelist():
            if name.endswith('/'):
                continue  # Skip directories
            basename = os.path.splitext(name)[0]
            if basename in xml_basenames:
                if basename not in groups:
                    groups[basename] = []
                groups[basename].append(name)

    return groups
