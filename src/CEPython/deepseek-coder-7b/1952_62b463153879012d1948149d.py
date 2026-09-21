import os
import xml.etree.ElementTree as ET


def _explore_folder(folder):
    """
    Get packages' data from folder

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    folder : str
        Folder of the package

    Returns
    -------
    dict
    """
    xml_files = {}
    for file in os.listdir(folder):
        if file.endswith(".xml"):
            xml_files[file] = os.path.join(folder, file)
    return xml_files
