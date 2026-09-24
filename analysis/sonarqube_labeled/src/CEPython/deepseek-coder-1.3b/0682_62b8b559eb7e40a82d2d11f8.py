

def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    # Convert the list of classes to a set to remove duplicates
    classes = set(classes)

    # Sort the list of classes in ascending order
    classes = sorted(list(classes))

    # Return the sorted list of classes
    return classes
