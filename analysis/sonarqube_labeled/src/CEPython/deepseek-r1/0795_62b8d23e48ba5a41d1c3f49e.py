def popitem(self):
    import random
    """
    Remove and return a random `(key, value)` pair.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    keys = list(self.keys())
    key = random.choice(keys)
    value = self.pop(key)
    return (key, value)
