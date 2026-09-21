

def popitem(self):
    """
    Remove and return the `(key, value)` pair first inserted.
    """
    if not self:
        raise KeyError('popitem(): dictionary is empty')
    for key in self:
        value = self[key]
        del self[key]
        return (key, value)
