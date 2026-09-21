

def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self.dict:
        return None

    least_recently_used_key = min(self.dict.keys(), key=lambda k: self.dict[k][1])
    least_recently_used_value = self.dict.pop(least_recently_used_key)

    return least_recently_used_key, least_recently_used_value
