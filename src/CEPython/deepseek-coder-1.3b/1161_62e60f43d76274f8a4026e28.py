from datetime import datetime
import pytz


def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: The number of nanoseconds since the epoch (1970-01-01 00:00:00 UTC)
    :param tz: A timezone object from the `pytz` library
    :return: A `Time` or `LocalTime` object
    """
    if tz is None:
        tz = pytz.UTC

    dt = datetime.utcfromtimestamp(nanoseconds / 1e9)
    return dt.replace(tzinfo=tz)
