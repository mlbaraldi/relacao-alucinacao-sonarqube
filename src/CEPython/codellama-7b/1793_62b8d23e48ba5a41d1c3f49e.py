

def popitem(self):
    # Get a random key from the dictionary
    key = random.choice(list(self.keys()))

    # Get the corresponding value
    value = self[key]

    # Remove the key-value pair from the dictionary
    del self[key]

    # Return the key-value pair
    return key, value
