from datetime import datetime
import pytz
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
    """
    # Convert the datetime to the new timezone
    dt_to_tz = self.from_tz.localize(dt, is_dst=None).astimezone(self.to_tz)

    # Check if the datetime is ambiguous and in a "fold" state
    if dt_to_tz.dst() != dt.dst():
        raise ValueError("The datetime is ambiguous and in a 'fold' state.")

    return dt_to_tz
