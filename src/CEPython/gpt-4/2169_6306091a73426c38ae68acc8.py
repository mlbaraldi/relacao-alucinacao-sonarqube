import os


def list_of_file_names(settings_dirs, spec_option):
    """
    Create a list of file names from given directories and a specific option
    """
    file_names = []
    for dir in settings_dirs:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if spec_option in file:
                    file_names.append(file)
    return file_names
