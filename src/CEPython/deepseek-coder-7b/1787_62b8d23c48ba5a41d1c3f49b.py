

def popitem(self):
    if not self.usage_order:
        raise KeyError("The cache is empty")
    key = self.usage_order.pop()
    value = self.cache.pop(key)
    return key, value
