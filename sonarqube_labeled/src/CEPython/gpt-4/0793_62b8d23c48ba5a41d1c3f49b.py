

def popitem(self):
    """
    Remove and return the `(key, value)` pair most recently used.
    """
    if self.dict:
        return self.dict.popitem()
    else:
        return None
