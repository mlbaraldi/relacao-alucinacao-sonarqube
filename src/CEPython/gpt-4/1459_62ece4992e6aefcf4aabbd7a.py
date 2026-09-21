import os


def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
    """
    shell = os.getenv('SHELL')
    return shell is not None and 'bash' in shell and os.name == 'nt'
