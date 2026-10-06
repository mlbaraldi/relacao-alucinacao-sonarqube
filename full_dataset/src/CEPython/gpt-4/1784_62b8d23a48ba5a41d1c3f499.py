from collections import OrderedDict


def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    try:
        key, value = self.cache.popitem(last=False)
    except KeyError:
        raise KeyError("Cache is empty")
    return key, value
