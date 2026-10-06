def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    # Remove duplicates while preserving order
    seen = set()
    unique = []
    for cls in classes:
        if cls not in seen:
            seen.add(cls)
            unique.append(cls)
    # Filter classes that are not superclasses of any others
    return [cls for cls in unique if not any(issubclass(other, cls) for other in unique if other != cls)]
