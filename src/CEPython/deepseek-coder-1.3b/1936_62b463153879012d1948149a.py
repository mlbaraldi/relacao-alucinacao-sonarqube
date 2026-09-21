

def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    xml_filename : str
        XML filenames
    files : list
        list of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: Package
    """
    grouped_files = {}
    for file in files:
        xml_basename = file.split('.')[0]
        if xml_basename in xmls:
            grouped_files[xml_basename] = xmls[xml_basename]
        else:
            grouped_files[xml_basename] = source
    return grouped_files
