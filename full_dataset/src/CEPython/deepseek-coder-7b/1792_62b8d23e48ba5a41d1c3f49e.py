import random


def popitem(self):
    """
    Remove and return a random `(key, value)` pair.
    """
    item = random.choice(list(self.items()))
    self.pop(item[0])
    return item
