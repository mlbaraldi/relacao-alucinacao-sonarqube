from zope.interface import directlyProvides, providedBy
from zope.interface import Interface, Attribute


def directlyProvidedBy(object):
    """
    Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
    # Get the interfaces directly provided by the object
    directly_provided_interfaces = providedBy(object) - providedBy(object).__bases__
    
    return directly_provided_interfaces

# Example usage:
