from datetime import datetime, time
import pytz


def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: The time in nanoseconds
    :param tz: The timezone
    :return: Time
    """
    if tz is None:
        tz = pytz.UTC
    else:
        tz = pytz.timezone(tz)

    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9

    # Create a datetime object from the seconds
    dt = datetime.fromtimestamp(seconds, tz)

    # Return only the time part
    return dt.time()
