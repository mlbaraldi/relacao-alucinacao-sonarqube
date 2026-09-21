import zipfile


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
    # Create a dictionary to store the data
    data = {}

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Iterate over all the files in the zip file
        for file in zip_ref.namelist():
            # Get the base name of the file
            base_name = file.split('/')[-1]

            # If the base name is not in the dictionary, add it
            if base_name not in data:
                data[base_name] = []

            # Add the file to the list of files with that base name
            data[base_name].append(file)

    return data
