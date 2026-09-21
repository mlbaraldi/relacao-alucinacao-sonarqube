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
    :param target_tz:
        A string representing the target timezone.
    :return:
        A timezone-aware :class:`datetime.datetime` object in the target timezone.
    """
    # Convert the datetime to a timezone-aware datetime
    aware_dt = pytz.utc.localize(dt)

    # Determine if the datetime is ambiguous
    if aware_dt.tzinfo.name != 'UTC':
        raise ValueError('The datetime must be in UTC')

    # Determine if the datetime is in a "fold" state
    if dt.date() == aware_dt.date():
        # If it is, find the first occurrence of the datetime
        first_occurrence = aware_dt
        while first_occurrence.date() == dt.date():
            first_occurrence = first_occurrence - datetime.timedelta(days=1)

        # Convert the first occurrence to the target timezone
        target_dt = first_occurrence.astimezone(pytz.timezone(target_tz))
    else:
        # If it's not, convert the datetime to the target timezone
        target_dt = aware_dt.astimezone(pytz.timezone(target_tz))
