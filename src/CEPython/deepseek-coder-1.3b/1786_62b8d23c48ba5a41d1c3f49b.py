

def popitem(self):
    if not self.my_dict:
        return None
    key, value = list(self.my_dict.items())[-1]
    del self.my_dict[key]
    return key, value
