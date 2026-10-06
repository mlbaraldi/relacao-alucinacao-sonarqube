

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
    size = size.upper()
    if 'K' in size:
        return int(size.replace('K', '')) * 1000
    elif 'M' in size:
        return int(size.replace('M', '')) * 1000**2
    elif 'G' in size:
        return int(size.replace('G', '')) * 1000**3
    elif 'T' in size:
        return int(size.replace('T', '')) * 1000**4
    elif 'P' in size:
        return int(size.replace('P', '')) * 1000**5
    else:
        return int(size)
