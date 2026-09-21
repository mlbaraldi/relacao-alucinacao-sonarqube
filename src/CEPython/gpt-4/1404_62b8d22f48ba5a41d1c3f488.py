

def popitem(self):
    try:
        key = next(iter(self))
    except StopIteration:
        raise KeyError('dictionary is empty')
    value = self.pop(key)
    return key, value
