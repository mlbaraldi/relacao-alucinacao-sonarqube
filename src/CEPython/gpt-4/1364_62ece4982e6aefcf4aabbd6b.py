

def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    subclasses_list = cls.__subclasses__()

    for subclass in cls.__subclasses__():
        subclasses_list.extend(subclasses(subclass))

    return subclasses_list
