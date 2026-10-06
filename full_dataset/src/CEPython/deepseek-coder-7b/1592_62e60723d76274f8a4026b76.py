import datetime


def from_ticks(cls, ticks, tz=None):
    """
    Create a time from ticks (nanoseconds since midnight).

    :param ticks: nanoseconds since midnight
    :type ticks: int
    :param tz: optional timezone
    :type tz: datetime.tzinfo

    :rtype: datetime.datetime

    :raises ValueError: if ticks is out of bounds
        (0 <= ticks < 86400000000000)
    """
    if not 0 <= ticks < 86400000000000:
        raise ValueError("ticks is out of bounds")

    # Calculate the number of days, hours, minutes, and seconds
    days = ticks // (24 * 60 * 60 * 1000000000)
    ticks %= (24 * 60 * 60 * 1000000000)
    hours = ticks // (60 * 60 * 1000000000)
    ticks %= (60 * 60 * 1000000000)
    minutes = ticks // (60 * 1000000000)
    ticks %= (60 * 1000000000)
    seconds = ticks // 1000000000
    ticks %= 1000000000

    # Create a datetime object
    dt = datetime.datetime(1, 1, 1, hours, minutes, seconds, ticks, tzinfo=tz) +
