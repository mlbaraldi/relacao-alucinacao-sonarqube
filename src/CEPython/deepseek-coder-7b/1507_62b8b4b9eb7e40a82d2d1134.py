

def namesAndDescriptions(self, all=False):
    """
    Return attribute names and descriptions defined by interface.
    """
    if all:
        # If all is True, return all attributes
        return self.attributes
    else:
        # If all is False, return only the names of the attributes
        return list(self.attributes.keys())
