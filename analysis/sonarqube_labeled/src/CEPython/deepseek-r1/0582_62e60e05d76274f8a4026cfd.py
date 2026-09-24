def index(self, key):
    for i in range(len(self)):
        if self[i] == key:
            return i
    raise ValueError(f"{repr(key)} is not in list")
