import datetime


def from_ticks(cls, ticks, tz=None):
    """
    Create a time from ticks (nanoseconds since midnight).

    :param ticks: nanoseconds since midnight
    :type ticks: int
    :param tz: optional timezone
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: if ticks is out of bounds
        (0 <= ticks < 86400000000000)
    """
    if not 0 <= ticks < 86400000000000:
        raise ValueError("ticks is out of bounds (0 <= ticks < 86400000000000)")

    # Convert ticks to seconds
    seconds = ticks / 1000000000

    # Create a datetime object
    dt = datetime.datetime(1, 1, 1, 0, 0, 0, tzinfo=tz) + datetime.timedelta(seconds=seconds)

    return cls(dt.timestamp() * 1000000000, tz)
