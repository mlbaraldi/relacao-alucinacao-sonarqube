def size_to_bytes(size: str) -> int:
    import re
    """
    Convert human readable file size to bytes.

    Resulting value is an approximation as input value is in most cases rounded.

    Args:
        size: A string representing a human readable file size (eg: '500K')

    Returns:
        A decimal representation of file size

    Examples:
        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
    """
    suffix_multiplier = {
        '': 1,
        'K': 10**3,
        'M': 10**6,
        'G': 10**9,
        'T': 10**12,
        'P': 10**15,
        'E': 10**18,
        'Z': 10**21,
        'Y': 10**24,
    }

    match = re.fullmatch(r'^(\d+\.?\d*|\.\d+)([A-Za-z])?$', size)
    if not match:
        raise ValueError(f"Invalid size format: {size}")

    numeric_str, suffix = match.groups()
    suffix = suffix.upper() if suffix else ''

    if suffix not in suffix_multiplier:
        raise ValueError(f"Invalid suffix: {suffix}")

    numeric = float(numeric_str)
    return int(numeric * suffix_multiplier[suffix])
