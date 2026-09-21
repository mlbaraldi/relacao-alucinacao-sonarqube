import re
import os
import shlex


def split(s, platform='this'):
    """
    Multi-platform variant of shlex.split() for command-line splitting.
    For use with subprocess, for argv injection etc. Using fast REGEX.

    platform: 'this' = auto from current platform;
              1 = POSIX;
              0 = Windows/CMD
              (other values reserved)
    """
    if platform == 'this':
        platform = 1 if os.name == 'posix' else 0

    if platform == 1:
        # POSIX
        args = shlex.split(s)
    elif platform == 0:
        # Windows/CMD
        args = re.findall(r'"[^"]*"|[^\s]+', s)
        args = [arg.replace('"', '') for arg in args]
    else:
        raise ValueError("Invalid platform value")

    return args
