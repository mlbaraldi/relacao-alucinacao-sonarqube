from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    # Calculate the range of the input list
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val

    # Calculate the scale factor
    scale_factor = 1.0 / range_val

    # Apply the scale factor to each element in the list
    rescaled_list = [scale_factor * (x - min_val) for x in numbers]

    return rescaled_list
