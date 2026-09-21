

def is_valid(self, identifier):
    """
    Return True if identifier is valid, False otherwise.
    """
    if not identifier:
        return False
    if not identifier[0].isalpha() and identifier[0] != '_':
        return False
    for char in identifier[1:]:
        if not char.isalnum() and char != '_':
            return False
    return True
