

def get(self, key, default=None):
    """
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    """
    if key in self.dict:
        return self.dict[key]
    else:
        return default
