import re


def get_pattern(pattern, strip=True):
    if strip:
        pattern = pattern.strip()
    pattern = re.escape(pattern)
    pattern = pattern.replace('*', '.*')
    pattern = pattern.replace('?', '.')
    return pattern
