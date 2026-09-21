def get_pattern(pattern, strip=True):
    import re
    """
    This method converts the given string to regex pattern
    """
    if strip:
        pattern = pattern.strip()
    processed = []
    for char in pattern:
        if char == '*':
            processed.append('.*')
        elif char == '?':
            processed.append('.')
        else:
            processed.append(re.escape(char))
    return ''.join(processed)
