from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    count = {}
    result = []

    # Count the occurrences of each number
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Add numbers to the result list if they occur only once
    for num in numbers:
        if count[num] == 1:
            result.append(num)

    return result
