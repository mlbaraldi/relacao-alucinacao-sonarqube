import re
import sys


def split(s, platform='this'):
    """
    Multi-platform variant of shlex.split() for command-line splitting.
    For use with subprocess, for argv injection etc. Using fast REGEX.

    platform: 'this' = auto from current platform;
              'POSIX' = POSIX;
              'Windows' = Windows/CMD
              (other values reserved)
    """
    if platform == 'this':
        platform = 'POSIX' if sys.platform.startswith('linux') else 'Windows'

    if platform == 'POSIX':
        # POSIX-compliant systems (like Linux or macOS)
        # Arguments are separated by whitespace and can be quoted with single or double quotes.
        return re.findall(r'\S+|\"([^\"]*)\"|\'([^\']*)\'', s)
    elif platform == 'Windows':
        # Windows Command Prompt (cmd.exe)
        # Arguments are separated by whitespace, but can be quoted with single or double quotes.
        # Also, escaping with ^ is supported.
        return re.findall(r'\S+|\"([^\"]*)\"|\'([^\']*)\'|\^([^\^]*)', s)
    else:
        raise ValueError("Unsupported platform")

# Example usage:
