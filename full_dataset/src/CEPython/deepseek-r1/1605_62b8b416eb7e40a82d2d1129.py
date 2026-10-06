def names(self, all=False):
    """
    Return the attribute names defined by the interface.
    """
    if all:
        attrs = set()
        for cls in self.__class__.mro():
            attrs.update(cls.__dict__.keys())
        return sorted(attrs)
    else:
        return sorted(self.__class__.__dict__.keys())
