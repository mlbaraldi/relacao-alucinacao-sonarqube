import re


def get_pattern(pattern, strip=True):
    """
    This method converts the given string to regex pattern
    """
    if strip:
        pattern = pattern.strip()
    pattern = re.escape(pattern)
    return pattern
