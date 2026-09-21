def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    candidates = []
    if explicit_mc is not None:
        candidates.append(explicit_mc)
    for base in bases:
        candidates.append(type(base))
    
    # Remove duplicates while preserving order
    unique = []
    for mc in candidates:
        if mc not in unique:
            unique.append(mc)
    candidates = unique
    
    if not candidates:
        return type
    
    for mc in candidates:
        if all(issubclass(mc, other) for other in candidates):
            return mc
    
    raise TypeError("metaclass conflict: no common derived metaclass")
