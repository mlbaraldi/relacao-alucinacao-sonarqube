

def setdefault(self, key, default=None):
    """
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    """
    if key not in self.data:
        self.data[key] = default
    return self.data.get(key, default)
