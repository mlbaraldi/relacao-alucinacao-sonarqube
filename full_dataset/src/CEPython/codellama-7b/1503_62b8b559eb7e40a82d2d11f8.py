

def minimalBases(classes):
    # Create a set of all the base classes
    base_classes = set(classes)

    # Iterate through the list of classes and remove any base classes that are already in the set
    for cls in classes:
        if cls in base_classes:
            base_classes.remove(cls)

    # Return the set of base classes
    return base_classes
