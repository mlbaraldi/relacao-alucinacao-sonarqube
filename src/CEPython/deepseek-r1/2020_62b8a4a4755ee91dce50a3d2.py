def _fromutc(self, dt):
    import bisect
    from datetime import datetime, timezone
    """
    Given a timezone-aware datetime in a given timezone, calculates a
    timezone-aware datetime in a new timezone.

    Since this is the one time that we *know* we have an unambiguous
    datetime object, we take this opportunity to determine whether the
    datetime is ambiguous and in a "fold" state.
    """
    if dt.tzinfo is None:
        raise ValueError("fromutc() requires a timezone-aware datetime")
    
    # Convert dt to UTC and extract as a naive datetime
    dt_utc = dt.astimezone(timezone.utc).replace(tzinfo=None)
    
    # Find the transition times and corresponding info
    transition_times = [trans[0] for trans in self._utc_transitions]
    transition_info = [trans[1] for trans in self._utc_transitions]
    
    # Find the index of the applicable transition
    idx = bisect.bisect_right(transition_times, dt_utc) - 1
    if idx >= 0:
        inf = transition_info[idx]
    else:
        # Default to the earliest known transition info
        inf = self._utc_transitions[0][1] if self._utc_transitions else (self._std_offset, self._dst_offset, self._tzname)
    
    offset, dstoffset, tzname = inf
    local_naive = dt_utc + offset
    
    # Check for ambiguity by comparing fold=0 and fold=1 offsets
    dt_fold0 = datetime(
        local_naive.year, local_naive.month, local_naive.day,
        local_naive.hour, local_naive.minute, local_naive.second,
        local_naive.microsecond, tzinfo=self, fold=0
    )
    dt_fold1 = datetime(
        local_naive.year, local_naive.month, local_naive.day,
        local_naive.hour, local_naive.minute, local_naive.second,
        local_naive.microsecond, tzinfo=self, fold=1
    )
    
    of0 = dt_fold0.utcoffset()
    of1 = dt_fold1.utcoffset()
    
    if of0 != of1:
        # Determine which fold corresponds to the current offset
        fold = 0 if (of0 == offset) else 1
    else:
        fold = 0
    
    return datetime(
        local_naive.year, local_naive.month, local_naive.day,
        local_naive.hour, local_naive.minute, local_naive.second,
        local_naive.microsecond, tzinfo=self, fold=fold
    )
