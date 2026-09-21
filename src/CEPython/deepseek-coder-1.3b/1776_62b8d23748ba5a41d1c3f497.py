

def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    least_frequent_item = min(self.dict, key=self.dict.count)
    popped_item = self.dict.pop(least_frequent_item)
    return least_frequent_item, popped_item
