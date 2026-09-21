

def parse_version(s: str) -> tuple[int, ...]:
    """
    poor man's version comparison
    """
    return tuple(int(i) for i in s.split('.'))
