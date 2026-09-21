

def values(self, *keys):
    if not keys:
        return list(self.values())
    else:
        return [self[key] for key in keys]
