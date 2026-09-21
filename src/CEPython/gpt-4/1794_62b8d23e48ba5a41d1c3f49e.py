import random


def popitem(self):
    """
    Remove and return a random `(key, value)` pair.
    """
    if not self.dict:
        raise KeyError("Dictionary is empty")

    key = random.choice(list(self.dict.keys()))
    value = self.dict.pop(key)

    return key, value
