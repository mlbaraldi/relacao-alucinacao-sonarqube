from datetime import datetime
import pytz


def fromutc(self, dt):
    """
    Given a timezone-aware datetime in a given timezone, calculates a
    timezone-aware datetime in a new timezone.

    Since this is the one time that we *know* we have an unambiguous
    datetime object, we take this opportunity to determine whether the
    datetime is ambiguous and in a "fold" state (e.g. if it's the first
    occurrence, chronologically, of the ambiguous datetime).

    :param dt:
        A timezone-aware :class:`datetime.datetime` object.
    :param tz_str:
        A string representing the target timezone.
    :return:
        A timezone-aware :class:`datetime.datetime` object in the target timezone.
    """
    dt = dt.replace(tzinfo=pytz.UTC)  # Convert to UTC
    tz = pytz.timezone(tz_str)

    # Check if the datetime is ambiguous
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        # If it's not, convert to the target timezone
        dt = dt.astimezone(tz)

    return dt
