from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    from typing import List
    from collections import Counter
    count = Counter(numbers)
    return [num for num in numbers if count[num] == 1]
