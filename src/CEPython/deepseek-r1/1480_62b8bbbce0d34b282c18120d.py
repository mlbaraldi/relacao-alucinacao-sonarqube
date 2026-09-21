def is_file_exist(file_name):
    import os
    """
    Check if file name exists as a regular file.
    :param file_name: File name.
    :type file_name: str
    :return: True if the file exists and is a regular file, False otherwise.
    :rtype: bool
    """
    return os.path.isfile(file_name)
