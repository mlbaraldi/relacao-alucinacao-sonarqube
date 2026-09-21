from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_deque = deque()
    result = []

    for num in numbers:
        while max_deque and max_deque[-1] < num:
            max_deque.pop()
        max_deque.append(num)
        result.append(max_deque[0])

    return result
