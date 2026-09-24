

def popitem(self):
    if len(self.order) == 0:
        return None
    else:
        key = self.order.pop(0)
        value = self[key]
        del self[key]
        del self.frequencies[key]
        return key, value
