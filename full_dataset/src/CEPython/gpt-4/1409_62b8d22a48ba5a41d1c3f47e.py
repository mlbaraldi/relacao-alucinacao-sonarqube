

def setdefault(self, key, default=None):
    """
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    """
    if key not in self.dict:
        self.dict[key] = default
    return self.dict.get(key, default)
