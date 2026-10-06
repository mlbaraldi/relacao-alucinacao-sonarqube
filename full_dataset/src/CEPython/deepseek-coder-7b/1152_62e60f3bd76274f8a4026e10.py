from datetime import timedelta


def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value: The timedelta object to be dehydrated.
    :type value: timedelta
    :return: A dictionary containing the days, seconds, and microseconds of the timedelta.
    :rtype: dict
    """
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }
