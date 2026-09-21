

def match(filename):
    """
    Check if the filename is a type that this module supports

    Args:
        filename: Filename to match
    Returns:
        False if not a match, True if supported
    """
    # Check if the file has a .txt extension
    if filename.endswith('.txt'):
        return True
    else:
        return False
