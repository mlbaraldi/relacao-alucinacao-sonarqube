from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_diff = float('inf')
    result = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < min_diff:
                min_diff = abs(numbers[i] - numbers[j])
                result = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    return result
