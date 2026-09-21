def unquote(name):
    """
    Remove quote from the given name.
    """
    if len(name) >= 2 and name[0] == name[-1] and name[0] in ('"', "'"):
        return name[1:-1]
    return name
