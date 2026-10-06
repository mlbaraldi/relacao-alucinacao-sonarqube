from typing import List


def concatenate(strings: List[str]) -> str:
    from typing import List
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
