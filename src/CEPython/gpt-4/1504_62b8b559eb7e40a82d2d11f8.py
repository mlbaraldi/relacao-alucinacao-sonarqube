

def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    minimal_bases = []
    for cls in classes:
        for base in minimal_bases:
            if issubclass(cls, base):
                break
        else:
            minimal_bases.append(cls)
    return minimal_bases
