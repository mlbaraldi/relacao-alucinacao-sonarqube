

def determineMetaclass(bases, explicit_mc=None):
    # If an explicit metaclass is provided, use it
    if explicit_mc is not None:
        return explicit_mc

    # If no explicit metaclass is provided, determine the metaclass from the bases
    metaclasses = [type(base) for base in bases]
    if len(metaclasses) == 1:
        return metaclasses[0]
    elif len(metaclasses) > 1:
        raise TypeError("Multiple metaclasses are not allowed")

    # If no metaclasses are found, use the default metaclass
    return type
