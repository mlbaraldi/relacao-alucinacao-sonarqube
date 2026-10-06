

def names(self, all=False):
    """
    Return the attribute names defined by the class.
    If all is True, return all attribute names including those inherited from the base classes.
    """
    if all:
        return [name for name in dir(self) if not name.startswith('__')]
    else:
        return [name for name in self.__dict__.keys() if not name.startswith('__')]
