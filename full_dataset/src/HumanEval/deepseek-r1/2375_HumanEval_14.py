from typing import List


def all_prefixes(string: str) -> List[str]:
    from typing import List
    return [string[:i] for i in range(1, len(string) + 1)]
