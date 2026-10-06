from datetime import datetime
import pytz


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
    :param from_tz:
        A string representing the name of the timezone the datetime is in.
    :param to_tz:
        A string representing the name of the timezone to convert to.
    """
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)

    # Localize the datetime to the from_tz timezone
    localized_dt = from_tz.localize(dt, is_dst=None)

    # Convert to the to_tz timezone
    converted_dt = localized_dt.astimezone(to_tz)

    return converted_dt
