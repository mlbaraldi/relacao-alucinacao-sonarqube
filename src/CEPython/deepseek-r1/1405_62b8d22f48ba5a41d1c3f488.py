def popitem(self):
    """
    Remove and return the `(key, value)` pair first inserted.
    """
    if not self.order:
        raise KeyError("popitem(): dictionary is empty")
    key = self.order.pop(0)
    value = self.data.pop(key)
    return (key, value)
