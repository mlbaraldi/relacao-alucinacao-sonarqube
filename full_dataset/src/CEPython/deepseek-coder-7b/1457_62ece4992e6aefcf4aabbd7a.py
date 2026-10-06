import os


def is_gitbash():
    """
    Returns True if you run in a Windows gitbash
    :return: True if gitbash
    """
    return 'GIT_INSTALL_ROOT' in os.environ

# Example usage:
