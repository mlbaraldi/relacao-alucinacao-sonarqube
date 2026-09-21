from datetime import time


def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: A datetime.time object.
    :type value: Time
    :return: A string representation of the time in the format 'HH:MM:SS'.
    :rtype: str
    """
    return value.strftime('%H:%M:%S')
