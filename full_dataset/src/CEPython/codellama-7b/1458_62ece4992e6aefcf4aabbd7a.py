import os


def is_gitbash():
    return os.environ.get('SHELL') == '/bin/bash'
