

def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    if explicit_mc is not None:
        return explicit_mc
    elif bases:
        return type('%sMeta' % bases[0].__name__, (object,), {})
    else:
        return object
