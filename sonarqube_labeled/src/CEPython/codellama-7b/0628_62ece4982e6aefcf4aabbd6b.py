

def subclasses(cls):
    subclasses = []
    for subclass in cls.__subclasses__():
        subclasses.append(subclass)
        subclasses.extend(subclasses(subclass))
    return subclasses
