

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

    size = size.strip()
    last_char = size[-1].upper()
    value = int(size[:-1])

    if last_char == 'K':
        return value * 1000
    elif last_char == 'M':
        return value * 1000 * 1000
    elif last_char == 'G':
        return value * 1000 * 1000 * 1000
    else:
        return value
