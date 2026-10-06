import zope.interface


def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative:
        if not iface.providedBy(candidate):
            raise zope.interface.Invalid("Candidate does not provide interface")

    for method in iface.getMethodNames():
        if not hasattr(candidate, method):
            raise zope.interface.Invalid("Candidate does not define method %s" % method)

        method_sig = iface.getMethodSignature(method)
        if not method_sig.isCompatibleWith(candidate.__getattr__(method).__code__):
            raise zope.interface.Invalid("Method %s has incorrect signature" % method)

    for attr in iface.getAttributeNames():
        if not hasattr(candidate, attr):
            raise zope.interface.Invalid("Candidate does not define attribute %s" % attr)

    return True
