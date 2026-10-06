def dehydrate_time(value):
    from datetime import Time
    """
    Dehydrator for `time` values.

    :param value: The time value to dehydrate.
    :type value: Time
    :return: ISO formatted time string.
    :rtype: str
    """
    return value.isoformat()
