from datetime import time


def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: Time object to be dehydrated
    :type value: datetime.time
    :return: Dehydrated time string in the format 'HH:MM:SS'
    :rtype: str
    """
    if isinstance(value, time):
        return value.strftime('%H:%M:%S')
    else:
        raise TypeError('Expected a datetime.time object')
