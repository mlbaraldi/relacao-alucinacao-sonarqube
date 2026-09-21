from datetime import datetime, timezone


def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: Nanoseconds to convert
    :param tz: Timezone for LocalTime, defaults to None
    :return: Time or LocalTime
    """
    if tz:
        return LocalTime(nanoseconds, tz)
    else:
        return Time(nanoseconds)
