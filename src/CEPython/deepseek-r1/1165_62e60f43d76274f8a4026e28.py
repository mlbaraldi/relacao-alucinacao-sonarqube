def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: Number of nanoseconds since midnight.
    :param tz: Timezone information if applicable.
    :return: Time or LocalTime instance.
    """
    HOUR_NS = 3600 * 10**9
    MINUTE_NS = 60 * 10**9
    SECOND_NS = 10**9

    hours, remaining = divmod(nanoseconds, HOUR_NS)
    minutes, remaining = divmod(remaining, MINUTE_NS)
    seconds, nanoseconds_remainder = divmod(remaining, SECOND_NS)

    if tz is not None:
        from neotime import Time
        return Time(hours, minutes, seconds, nanoseconds_remainder, tzinfo=tz)
    else:
        from neotime import LocalTime
        return LocalTime(hours, minutes, seconds, nanoseconds_remainder)
