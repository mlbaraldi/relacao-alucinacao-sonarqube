import inspect


def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    return [c for c in inspect.getmembers(cls, inspect.isclass)]
