

def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    # If an explicit metaclass is provided, use it
    if explicit_mc is not None:
        return explicit_mc

    # If there's only one base, use its metaclass
    if len(bases) == 1:
        base = bases[0]
        if isinstance(base, type):
            return base

    # If no metaclass is found, use type as the default
    return type
