def namesAndDescriptions(self, all=False):
    """
    Return attribute names and descriptions defined by interface.
    """
    interface_cls = self.__class__
    attrs = []
    seen = set()
    if all:
        for cls in interface_cls.__mro__:
            for name, attr in cls.__dict__.items():
                if isinstance(attr, InterfaceAttribute):
                    if name not in seen:
                        seen.add(name)
                        attrs.append((name, attr.description))
    else:
        for name, attr in interface_cls.__dict__.items():
            if isinstance(attr, InterfaceAttribute):
                attrs.append((name, attr.description))
    return attrs
