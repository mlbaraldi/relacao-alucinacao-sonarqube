import datetime


def hydrate_time(nanoseconds, tz=None):
    if tz is None:
        tz = datetime.timezone.utc
    return datetime.time(nanoseconds, tz=tz)
