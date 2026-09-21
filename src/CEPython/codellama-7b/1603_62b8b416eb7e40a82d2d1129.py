

def names(self, all=False):
    if all:
        return [name for name in self.__dict__ if not name.startswith('_')]
    else:
        return [name for name in self.__dict__ if not name.startswith('_') and not name.endswith('_')]
