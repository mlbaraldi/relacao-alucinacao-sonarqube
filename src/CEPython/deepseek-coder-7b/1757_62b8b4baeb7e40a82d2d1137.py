from zope.interface import providedBy, implementedBy


def verifyObject(iface, candidate, tentative=False):
    if not tentative and not iface.providedBy(candidate):
        raise ValueError(f"{candidate} does not provide {iface}")

    if not iface.implementedBy(candidate):
        raise ValueError(f"{candidate} does not implement {iface}")

    for attr in iface.names():
        if not hasattr(candidate, attr):
            raise ValueError(f"{candidate} does not have attribute {attr}")

    for method in iface.names():
        if not hasattr(candidate, method):
            raise ValueError(f"{candidate} does not have method {method}")

    return True
