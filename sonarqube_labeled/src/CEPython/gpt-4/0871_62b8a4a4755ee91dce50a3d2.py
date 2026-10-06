import pytz
from datetime import datetime


def _fromutc(self, dt):
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
        raise ValueError("The datetime object must be timezone-aware")

    # Convert the datetime to the new timezone
    new_dt = dt.astimezone(self.new_timezone)

    # Check if the datetime is ambiguous (i.e., it occurs twice due to a DST transition)
    if pytz.datetime_ambiguous(new_dt):
        # If the datetime is ambiguous, determine whether it's in a "fold" state
        if pytz.datetime_exists(new_dt.replace(fold=1)):
            new_dt = new_dt.replace(fold=1)
        else:
            new_dt = new_dt.replace(fold=0)

    return new_dt
