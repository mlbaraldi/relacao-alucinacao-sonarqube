import os


def is_gitbash():
    """
    Returns True if you run in a Windows gitbash

    :return: True if gitbash
    """
    return 'WT_SESSION' in os.environ
