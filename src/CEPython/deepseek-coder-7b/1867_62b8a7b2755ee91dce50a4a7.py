from datetime import datetime
from dateutil.tz import tzoffset
from dateutil.tz import tzoffset
from dateutil.parser import parse


def default_tzinfo(dt, tzinfo):
    """
    Sets the ``tzinfo`` parameter on naive datetimes only

    This is useful for example when you are provided a datetime that may have
    either an implicit or explicit time zone, such as when parsing a time zone
    string.

    :param dt: The datetime on which to replace the time zone
    :param tzinfo: The datetime.tzinfo subclass instance to assign to dt if (and only if) it is naive.
    :return: Returns an aware datetime.datetime.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tzinfo)
    return dt
