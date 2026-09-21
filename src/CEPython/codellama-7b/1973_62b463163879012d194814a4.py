import zipfile


def _explore_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        file_names = zip_file.namelist()
        file_data = {}
        for file_name in file_names:
            if file_name.endswith('.xml'):
                file_data[file_name] = zip_file.read(file_name)
    return file_data
