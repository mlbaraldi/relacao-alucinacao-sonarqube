

def from_raw_values(cls, values):
    """
    Create a Bookmarks object from a list of raw bookmark string values.

    :param values: ASCII string values (raw bookmarks)
    :type values: Iterable[str]
    """
    return cls(values)

# Example usage:
