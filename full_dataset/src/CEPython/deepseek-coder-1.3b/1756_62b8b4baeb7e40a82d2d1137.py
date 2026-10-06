from zope.interface import Interface, implementer, providedBy


def verifyObject(iface, candidate, tentative=False):
    """
    Verify that *candidate* might correctly provide *iface*.
    """
    if not tentative:
        if not iface.providedBy(candidate):
            raise ValueError("The candidate does not provide the interface.")

    implemented_by = providedBy(candidate)
    if not set(implemented_by).issuperset(iface.__implemented__):
        raise ValueError("The candidate does not implement the interface.")

    for method in iface.methods:
        if method not in implemented_by.methods:
            raise ValueError("The candidate does not provide the method {}.".format(method))

    for attribute in iface.attributes:
        if attribute not in implemented_by.attributes:
            raise ValueError("The candidate does not provide the attribute {}.".format(attribute))

    return True
