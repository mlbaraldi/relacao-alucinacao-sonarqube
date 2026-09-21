

def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    xmls : list
        list of XML filenames
    files : list
        list of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: list of files associated with the XML
    """
    grouped_files = {}
    for xml in xmls:
        base_name = os.path.splitext(xml)[0]  # get the base name of the xml file
        associated_files = [file for file in files if base_name in file]  # find files associated with the xml
        grouped_files[xml] = associated_files
    return grouped_files
