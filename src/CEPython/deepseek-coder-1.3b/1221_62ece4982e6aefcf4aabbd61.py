

def _dictsum(dicts):
    """
    Combine values of the dictionaries supplied by iterable dicts.

    >>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
    {'a': 6, 'b': 2}
    """
    return {k: sum(v for k, v in d.items() if k in d) for d in dicts}
