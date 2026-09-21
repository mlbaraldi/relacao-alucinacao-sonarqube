def pop(self, key, default=__marker):
    if key in self.data:
        value = self.data[key]
        del self.data[key]
        return value
    else:
        if default is not self.__marker:
            return default
        else:
            raise KeyError(key)
