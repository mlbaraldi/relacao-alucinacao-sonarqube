import pytz
from datetime import datetime


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
    if dt.tzinfo is None:
        raise ValueError("Datetime object is not timezone-aware")

    # Convert to the new timezone
    new_dt = dt.astimezone(self.timezone)

    # Check if the datetime is ambiguous (i.e., it's in a "fold" state)
    if pytz.datetime_ambiguous(new_dt):
        print("Warning: The datetime is ambiguous (in a 'fold' state).")

    return new_dt
