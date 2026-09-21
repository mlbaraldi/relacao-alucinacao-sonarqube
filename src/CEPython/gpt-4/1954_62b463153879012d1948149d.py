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
    # Initialize an empty dictionary
    data_dict = {}

    # Iterate over all files in the folder
    for filename in os.listdir(folder):
        # Check if the file is an XML file
        if filename.endswith('.xml'):
            # Get the basename of the file
            basename = os.path.basename(filename)
            # Remove the .xml extension from the basename
            basename = os.path.splitext(basename)[0]

            # Parse the XML file
            tree = ET.parse(os.path.join(folder, filename))
            root = tree.getroot()

            # Initialize an empty dictionary for this file
            file_dict = {}

            # Iterate over all elements in the XML file
            for elem in root:
                # Add the element's tag and text to the file dictionary
                file_dict[elem.tag] = elem.text

            # Add the file dictionary to the data dictionary
            data_dict[basename] = file_dict

    # Return the data dictionary
    return data_dict
