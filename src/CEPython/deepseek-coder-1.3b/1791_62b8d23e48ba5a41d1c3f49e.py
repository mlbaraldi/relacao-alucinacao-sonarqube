import random


def popitem(self):
    """
    Remove and return a random `(key, value)` pair.
    """
    if not self.dictionary:
        return None

    random_key = random.choice(list(self.dictionary.keys()))
    popped_item = self.dictionary.pop(random_key)
    return random_key, popped_item
