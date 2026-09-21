import re


def parse_version(s: str) -> tuple[int, ...]:
    """
    poor man's version comparison
    """
    version_parts = re.split('(\d+)', s)
    version_parts = [part for part in version_parts if part]
    return tuple(int(part) for part in version_parts)
