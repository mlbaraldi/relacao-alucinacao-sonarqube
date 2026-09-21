def from_raw_values(cls, values):
    """
    Create a Bookmarks object from a list of raw bookmark string values.

    You should not need to use this method unless you want to deserialize
    bookmarks.

    :param values: ASCII string values (raw bookmarks)
    :type values: Iterable[str]
    """
    validated_values = []
    for value in values:
        if not isinstance(value, str):
            raise TypeError(f"Expected a string, got {type(value).__name__}")
        if not value.isascii():
            raise ValueError(f"Value {value!r} contains non-ASCII characters")
        validated_values.append(value)
    return cls(validated_values)
