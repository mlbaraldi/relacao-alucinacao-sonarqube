import os
import sys


def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    normalized_cmd = []
    for arg in cmd:
        if arg.startswith('python'):
            normalized_cmd.append(arg)
        elif arg.startswith('python3'):
            normalized_cmd.append(arg)
        elif arg.startswith('py'):
            normalized_cmd.append(arg)
        elif arg.startswith('pypy'):
            normalized_cmd.append(arg)
        elif arg.startswith('pypy3'):
            normalized_cmd.append(arg)
        elif arg.startswith('pysh'):
            normalized_cmd.append(arg)
        elif arg.startswith('pysh3'):
            normalized_cmd.append(arg)
        elif arg.startswith('python'):
            normalized_cmd.append(arg)
        elif arg.startswith('python3'):
            normalized_cmd.append(arg)
        elif arg.startswith('py'):
            normalized_cmd.append(arg)
        elif arg.startswith('pypy'):
            normalized_cmd.append(arg)
        elif arg.startswith('pypy3'):
            normalized_cmd.append(arg)
        elif arg.startswith('pysh'):
            normalized_cmd.append(arg)
        elif arg.startswith('pysh3'):
            normalized_cmd.append(arg)
        else:
            normalized_cmd.append(os.path.normpath(arg))
    return tuple(normalized_cmd)
