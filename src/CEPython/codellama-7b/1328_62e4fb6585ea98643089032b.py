

def parse_version(s: str) -> tuple[int, ...]:
    version_parts = s.split('.')
    version_numbers = []
    for part in version_parts:
        try:
            version_numbers.append(int(part))
        except ValueError:
            version_numbers.append(0)
    return tuple(version_numbers)
