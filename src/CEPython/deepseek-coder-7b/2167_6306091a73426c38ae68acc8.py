import os


def list_of_file_names(settings_dirs, spec_option):
    """
    List all files in the specified directories with a specific extension.

    :param settings_dirs: A list of directory paths.
    :param spec_option: The file extension to filter by.
    :return: A list of file names with the specified extension in the given directories.
    """
    file_list = []
    for directory in settings_dirs:
        for filename in os.listdir(directory):
            if filename.endswith(spec_option):
                file_list.append(filename)
    return file_list
