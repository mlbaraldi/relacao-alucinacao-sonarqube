from datetime import datetime, tzinfo
from dateutil.tz import tzoffset
from dateutil.parser import parse
from dateutil.utils import default_tzinfo


def default_tzinfo(dt, tzinfo):
    if dt.tzinfo is None:
        return tzinfo.localize(dt)
    else:
        return dt
