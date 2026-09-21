def popitem(self):
    from collections import OrderedDict
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self.key_map:
        raise KeyError("Cache is empty")
    
    # Get the OrderedDict for the current minimum frequency
    ordered_dict = self.freq_map[self.min_freq]
    
    # Pop the least recently used key (first item in OrderedDict)
    key, _ = ordered_dict.popitem(last=False)
    value, _ = self.key_map.pop(key)
    
    # If the OrderedDict is now empty, remove the frequency entry and update min_freq
    if not ordered_dict:
        del self.freq_map[self.min_freq]
        # Find the new minimum frequency if there are remaining entries
        if self.freq_map:
            self.min_freq = min(self.freq_map.keys())
        else:
            self.min_freq = 0  # Reset as cache is empty
    
    return (key, value)
