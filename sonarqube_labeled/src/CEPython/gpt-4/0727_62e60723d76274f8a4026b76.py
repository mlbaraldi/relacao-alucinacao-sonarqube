from datetime import time, tzinfo


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
        raise ValueError("Ticks is out of bounds (0 <= ticks < 86400000000000)")

    # Convert ticks to seconds
    seconds = ticks // 1000000000

    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # Create time object
    return time(hour=hours, minute=minutes, second=seconds, tzinfo=tz)
