import re


def is_valid(self, identifier):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', identifier):
        return False
    return True
