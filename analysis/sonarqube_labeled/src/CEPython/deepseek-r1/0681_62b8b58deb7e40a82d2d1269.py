def directlyProvidedBy(object):
    from zope.interface.declarations import Declaration
    from zope.interface.interface import InterfaceClass
    if isinstance(object, InterfaceClass):
        return _empty
    elif isinstance(object, type):
        return getattr(object, '__implemented__', _empty)
    else:
        provided = getattr(object, '__provided__', _empty)
        return provided if provided is not None else _empty
