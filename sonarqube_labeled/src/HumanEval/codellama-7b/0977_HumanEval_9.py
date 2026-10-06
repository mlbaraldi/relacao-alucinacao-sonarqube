from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        max_value = max(numbers[i:])
        result.append(max_value)
    return result
