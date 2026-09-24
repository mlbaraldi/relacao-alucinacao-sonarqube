import datetime


def from_ticks(cls, ticks, tz=None):
    if tz is None:
        tz = datetime.timezone.utc
    return cls(ticks, tz)
