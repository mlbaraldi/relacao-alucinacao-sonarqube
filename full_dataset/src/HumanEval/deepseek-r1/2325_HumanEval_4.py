from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    from typing import List
    mean = sum(numbers) / len(numbers)
    absolute_differences = [abs(x - mean) for x in numbers]
    return sum(absolute_differences) / len(numbers)
