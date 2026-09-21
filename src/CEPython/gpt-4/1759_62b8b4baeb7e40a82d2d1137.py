from zope.interface import Invalid, providedBy, Interface
from zope.interface.verify import verifyObject as zope_verifyObject


def verifyObject(iface, candidate, tentative=False):
    """
    Verify that *candidate* might correctly provide *iface*.

    :return bool: Returns a true value if everything that could be
       checked passed.
    :raises zope.interface.Invalid: If any of the previous
       conditions does not hold.
    """
    if not isinstance(iface, Interface):
        raise Invalid("iface must be an instance of Interface")

    if not tentative:
        if not iface.providedBy(candidate):
            raise Invalid("Candidate does not claim to provide the interface")

    try:
        zope_verifyObject(iface, candidate)
    except Invalid as e:
        raise Invalid("Candidate does not correctly provide the interface: " + str(e))

    return True
