

def popitem(self):
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key, value = next(iter(self.items()))
    del self[key]
    return key, value
