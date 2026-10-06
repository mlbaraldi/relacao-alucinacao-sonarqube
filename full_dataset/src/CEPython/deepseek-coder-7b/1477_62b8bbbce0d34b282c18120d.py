import os


def is_file_exist(file_name):
    """
    Check if file name exists.
    :param file_name: File name.
    :type file_name: str
    :return: Return True if the file exists, False otherwise.
    :rtype: bool
    """
    return os.path.isfile(file_name)

# Example usage:
