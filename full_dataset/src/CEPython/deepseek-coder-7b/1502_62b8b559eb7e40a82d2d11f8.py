

def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    return sorted(set(classes), key=classes.index)
