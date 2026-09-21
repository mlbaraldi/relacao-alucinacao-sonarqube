import zipfile
import os


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
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_dict = {}
        for file in zip_ref.namelist():
            if file.endswith('.xml'):
                base = os.path.splitext(os.path.basename(file))[0]
                if base not in file_dict:
                    file_dict[base] = []
                file_dict[base].append(file)
        return file_dict
