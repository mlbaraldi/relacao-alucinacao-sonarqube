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
        raise ValueError("ticks is out of bounds")
    total_seconds, nanoseconds = divmod(ticks, 10**9)
    hours, remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    return cls(hours, minutes, seconds, nanoseconds, tzinfo=tz)
