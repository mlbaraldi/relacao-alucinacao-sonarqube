from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    from typing import List
    if not numbers:
        return []
    result = []
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimeter)
    result.append(numbers[-1])
    return result
