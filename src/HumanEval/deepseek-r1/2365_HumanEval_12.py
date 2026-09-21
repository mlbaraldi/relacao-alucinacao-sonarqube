from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    from typing import List, Optional
    longest_str = None
    max_length = -1
    for s in strings:
        current_length = len(s)
        if current_length > max_length:
            max_length = current_length
            longest_str = s
    return longest_str
