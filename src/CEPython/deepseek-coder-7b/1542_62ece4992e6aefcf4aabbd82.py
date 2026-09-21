import re


def get_pattern(pattern, strip=True):
    """
    This method escapes special characters in the given string to make it a regex pattern
    """
    # Escape special characters
    escaped_pattern = re.escape(pattern)
    
    # If strip is True, remove the start and end delimiters
    if strip:
        escaped_pattern = escaped_pattern[1:-1]
    
    return escaped_pattern
