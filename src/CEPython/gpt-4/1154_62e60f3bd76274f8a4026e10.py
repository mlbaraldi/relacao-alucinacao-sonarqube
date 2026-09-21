from datetime import timedelta


def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value: timedelta value to dehydrate
    :type value: timedelta
    :return: string representation of timedelta
    :rtype: str
    """
    total_seconds = int(value.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{days}d {hours}h {minutes}m {seconds}s'
