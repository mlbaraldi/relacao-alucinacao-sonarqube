

def popitem(self):
    if len(self.cache) == 0:
        return None
    else:
        key, value = self.cache.popitem()
        self.order.remove(key)
        return key, value
