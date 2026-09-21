

def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    if explicit_mc is not None:
        return explicit_mc

    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type

    metaclass = metaclasses[0]
    for mc in metaclasses[1:]:
        if issubclass(mc, metaclass):
            metaclass = mc
        elif not issubclass(metaclass, mc):
            raise TypeError("Incompatible metaclasses")

    return metaclass
