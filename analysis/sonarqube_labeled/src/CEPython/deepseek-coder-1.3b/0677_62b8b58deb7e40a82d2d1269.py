from zope.interface import Interface


def directlyProvidedBy(object):
    """
    Return the interfaces directly provided by the given object
    """
    return object.providedBy()
