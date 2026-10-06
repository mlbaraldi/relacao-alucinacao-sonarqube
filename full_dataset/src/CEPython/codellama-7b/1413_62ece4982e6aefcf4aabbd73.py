import re


def split(s, platform='this'):
    if platform == 'this':
        platform = 1 if os.name == 'posix' else 0
    if platform == 1:
        # POSIX
        return re.split(r'(\s+|"(?:\\.|[^"])*")', s)
    elif platform == 0:
        # Windows/CMD
        return re.split(r'(\s+|"(?:\\.|[^"])*")', s)
    else:
        raise ValueError('Invalid platform')
