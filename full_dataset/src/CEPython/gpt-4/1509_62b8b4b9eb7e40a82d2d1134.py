

def namesAndDescriptions(self, all=False):
    """
    Return attribute names and descriptions defined by interface.
    """
    result = []
    for attr in dir(self):
        if all or not attr.startswith('_'):  # skip private attributes if all is False
            doc = getattr(self, attr).__doc__  # get the docstring
            if doc is not None:
                result.append((attr, doc))
    return result
