import os
import sys


def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    if sys.platform == "win32":
        # Fix for https://bugs.python.org/issue8557
        if cmd[0].startswith("#!"):
            cmd[0] = cmd[0][2:]

        # Make deep-path shebangs work
        if cmd[0].startswith("/"):
            cmd[0] = cmd[0][1:]

    return cmd
