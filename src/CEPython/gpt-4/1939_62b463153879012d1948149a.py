import os


def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    source : str
        Source directory or zipfile
    xmls : list
        List of XML filenames
    files : list
        List of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: Package
    """
    grouped_files = {}

    for xml in xmls:
        xml_basename = os.path.basename(xml)
        grouped_files[xml_basename] = []

    for file in files:
        file_basename = os.path.basename(file)
        if file_basename in grouped_files:
            grouped_files[file_basename].append(file)

    return grouped_files
