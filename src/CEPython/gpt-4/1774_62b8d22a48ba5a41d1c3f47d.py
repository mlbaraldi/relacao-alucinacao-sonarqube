

def pop(self, key, default=__marker):
    if key in self.dict:
        value = self.dict[key]
        del self.dict[key]
        return value
    elif default is not None:
        return default
    else:
        raise KeyError('Key not found')
