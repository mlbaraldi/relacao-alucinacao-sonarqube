import time


def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: A time object
    :type value: time.struct_time
    :return: A string in the format 'Day DD Month YYYY HH:MM:SS'
    :rtype: str
    """
    return time.strftime('%A %d %B %Y %H:%M:%S', value)
