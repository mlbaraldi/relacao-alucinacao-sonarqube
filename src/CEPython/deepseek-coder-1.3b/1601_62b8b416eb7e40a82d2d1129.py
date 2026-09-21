import inspect


def names(self, all=False):
    """
    Return the attribute names defined by the interface.
    """
    return [a[0] for a in inspect.getmembers(self, inspect.isfunction)]
