from datetime import timedelta
from datetime import timedelta


def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value:
    :type value: timedelta
    :return:
    """
    total_seconds = int(value.total_seconds())
    days = total_seconds // (24*60*60)
    hours = (total_seconds // (60*60)) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    return "{} days, {} hours, {} minutes, and {} seconds".format(days, hours, minutes, seconds)
