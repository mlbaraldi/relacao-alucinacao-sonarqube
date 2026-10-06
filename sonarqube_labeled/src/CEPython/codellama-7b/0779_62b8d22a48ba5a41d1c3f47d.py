

def pop(self, key, default=__marker):
    if key in self.data:
        value = self.data[key]
        del self.data[key]
        return value
    elif default is not None:
        return default
    else:
        raise KeyError(f"Key {key} not found in dictionary")
