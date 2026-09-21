from collections import OrderedDict


def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self.cache:
        raise KeyError("Cache is empty")
    # Pop the least frequently used key
    key, value = self.cache.popitem(last=False)
    return key, value
