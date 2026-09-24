from dateutil.parser import isoparse
from dateutil.tz import tzoffset, tzutc
import datetime


def isoparse(self, dt_str):
    try:
        dt = isoparse(dt_str)
        if dt.tzinfo is None:
            return dt
        elif dt.tzinfo.utcoffset(None) == datetime.timedelta(0):
            return dt.replace(tzinfo=tzutc())
        else:
            return dt
    except ValueError:
        raise ValueError("Invalid ISO-8601 datetime string")
