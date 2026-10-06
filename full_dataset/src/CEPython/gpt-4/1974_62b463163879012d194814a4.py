import os
import zipfile
from collections import defaultdict


def _explore_zipfile(zip_path):
    """
    Get packages' data from zip_path

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    zip_path : str
        zip file path
    Returns
    -------
    dict
    """
    # Create a dictionary to store the files
    files_dict = defaultdict(list)

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Loop over each file
        for file in zip_ref.namelist():
            # Check if the file is an XML file
            if file.endswith('.xml'):
                # Get the base name of the file
                base_name = os.path.basename(file)
                # Add the file to the dictionary
                files_dict[base_name].append(file)

    # Return the dictionary
    return files_dict
