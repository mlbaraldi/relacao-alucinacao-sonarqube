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
    data = {}

    # Iterate over all files in the folder and its subfolders
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Check if the file is an XML file
            if file.endswith('.xml'):
                # Parse the XML file
                tree = ET.parse(os.path.join(root, file))
                root = tree.getroot()

                # Extract the XML base name
                base_name = os.path.splitext(file)[0]

                # Store the data in the dictionary
                data[base_name] = {}
                for child in root:
                    data[base_name][child.tag] = child.text

    return data
