from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset, tzutc


def isoparse(self, dt_str):
    dt = parse(dt_str)

    # Handle midnight
    if dt.hour == 24:
        dt = dt.replace(hour=0)

    # Handle UTC
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tzutc())

    return dt
