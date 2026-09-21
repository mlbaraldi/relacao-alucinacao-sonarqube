from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    from typing import List
    """ From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence. """
    if not numbers:
        return []
    result = [numbers[0]]
    current_max = numbers[0]
    for num in numbers[1:]:
        current_max = max(current_max, num)
        result.append(current_max)
    return result
