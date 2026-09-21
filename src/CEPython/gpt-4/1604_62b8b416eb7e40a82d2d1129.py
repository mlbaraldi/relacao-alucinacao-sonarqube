

def names(self, all=False):
    """
    Return the attribute names defined by the interface.
    """
    if all:
        return [attr for attr in self.__dict__.keys() if not callable(getattr(self, attr))]
    else:
        return [attr for attr in self.__dict__.keys() if not attr.startswith("__") and not callable(getattr(self, attr))]
