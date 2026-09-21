def fromutc(self, dt):
    from datetime import timezone
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
        raise ValueError("dt must be a timezone-aware datetime")

    # Convert the input datetime to UTC
    utc_time = dt.astimezone(timezone.utc)

    # Convert UTC time to the target timezone to get a naive local time
    local_aware = utc_time.astimezone(self)
    naive_local = local_aware.replace(tzinfo=None)

    # Check if this naive local time is ambiguous in the target timezone
    dt_fold0 = naive_local.replace(fold=0)
    dt_fold1 = naive_local.replace(fold=1)

    offset0 = self.utcoffset(dt_fold0)
    offset1 = self.utcoffset(dt_fold1)

    if offset0 != offset1:
        # Determine which fold corresponds to the original UTC time
        utc_candidate0 = dt_fold0 - offset0
        utc_candidate1 = dt_fold1 - offset1

        if utc_candidate0 == utc_time:
            fold = 0
        elif utc_candidate1 == utc_time:
            fold = 1
        else:
            raise ValueError("Could not resolve ambiguity; no matching UTC time")
    else:
        # Not ambiguous, use the fold from the original conversion
        fold = local_aware.fold

    # Construct the resulting datetime with the correct fold and timezone
    return naive_local.replace(tzinfo=self, fold=fold)
