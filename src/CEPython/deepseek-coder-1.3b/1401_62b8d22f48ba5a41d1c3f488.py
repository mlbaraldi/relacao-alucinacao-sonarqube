

def popitem(self):
    """
    Remove and return the `(key, value)` pair first inserted.
    """
    if not self.my_dict:
        return None
    key, value = list(self.my_dict.items())[0]
    del self.my_dict[key]
    return key, value
