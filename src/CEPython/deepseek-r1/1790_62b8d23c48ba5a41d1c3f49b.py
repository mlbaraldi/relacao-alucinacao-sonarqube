def popitem(self):
    from collections import OrderedDict
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    return super().popitem(last=True)
