def dehydrate_timedelta(value):
    from datetime import timedelta
    """
    Dehydrator for `timedelta` values.

    :param value: The timedelta object to dehydrate.
    :type value: timedelta
    :return: A dictionary with 'days', 'seconds', and 'microseconds' as keys.
    :rtype: dict
    """
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }
