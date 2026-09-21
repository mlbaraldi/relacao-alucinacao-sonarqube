def values(self, *keys):
    if not keys:
        return [self[i] for i in range(len(self))]
    return [self[key] for key in keys]
