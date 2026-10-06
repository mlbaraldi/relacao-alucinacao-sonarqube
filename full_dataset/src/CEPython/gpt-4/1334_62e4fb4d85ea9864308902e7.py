import os
import sys


def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    if sys.platform == 'win32':
        # Fix for Python bug 8557.
        cmd = tuple(os.path.normpath(c) for c in cmd)

        # Windows does not parse shebangs. We need to explicitly call the Python interpreter.
        if cmd[0].endswith('.py'):
            cmd = ('python',) + cmd

    return cmd
