import zipfile
import os


def files_list_from_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return [file.filename for file in zip_ref.filelist]

# Test the function
