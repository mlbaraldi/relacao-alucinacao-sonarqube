

def index(self, key):
    for i, item in enumerate(self):
        if item == key:
            return i
    return -1
