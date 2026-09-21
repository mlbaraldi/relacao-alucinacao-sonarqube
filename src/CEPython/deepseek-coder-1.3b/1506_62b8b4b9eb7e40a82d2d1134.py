

def namesAndDescriptions(self, all=False):
    """
    Return attribute names and descriptions defined by interface.
    """
    attributes = dir(self)
    result = {}

    for attribute in attributes:
        if not attribute.startswith("__"):
            attribute_obj = getattr(self, attribute)
            if hasattr(attribute_obj, "__doc__"):
                result[attribute] = attribute_obj.__doc__

    return result
