from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    from typing import List, Any
    """ Filter given list of any python values only for integers """
    return [x for x in values if type(x) == int]
