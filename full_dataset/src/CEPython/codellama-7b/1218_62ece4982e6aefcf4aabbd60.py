

def size_to_bytes(size: str) -> int:
    """
    Convert human readable file size to bytes.

    Resulting value is an approximation as input value is in most case rounded.

    Args:
        size: A string representing a human readable file size (eg: '500K')

    Returns:
        A decimal representation of file size

    Examples::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
    """
    size_unit = size[-1]
    size_value = float(size[:-1])

    if size_unit == "K":
        return int(size_value * 1000)
    elif size_unit == "M":
        return int(size_value * 1000000)
    elif size_unit == "G":
        return int(size_value * 1000000000)
    else:
        return int(size_value)
