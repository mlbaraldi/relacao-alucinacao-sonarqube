import shlex
import re


def split(s, platform='this'):
    if platform == 'this':
        platform = '0' if 'win' in str(platform).lower() else '1'

    if platform == '1':
        # POSIX-style splitting
        return shlex.split(s)
    elif platform == '0':
        # Windows/CMD-style splitting
        return re.split(r'(\s+)', s)
    else:
        raise ValueError('Invalid platform value. Valid values are 1 (POSIX) or 0 (Windows/CMD).')
