

def data(self, *keys):
    result = {}
    if not keys:
        return self.__dict__
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self.__dict__):
                raise IndexError('Index out of bounds')
            key = list(self.__dict__.keys())[key]
        result[key] = self.__dict__.get(key, None)
    return result
