import zope.interface


def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative:
        if not iface.providedBy(candidate):
            raise zope.interface.Invalid("Candidate does not provide interface")

    methods = zope.interface.interface.MethodsOf(iface)
    for method in methods:
        if not hasattr(candidate, method):
            raise zope.interface.Invalid("Candidate does not define necessary method: " + method)
        if not callable(getattr(candidate, method)):
            raise zope.interface.Invalid("Candidate's method is not callable: " + method)

    attributes = zope.interface.interface.AttributesOf(iface)
    for attribute in attributes:
        if not hasattr(candidate, attribute):
            raise zope.interface.Invalid("Candidate does not define necessary attribute: " + attribute)

    return True
