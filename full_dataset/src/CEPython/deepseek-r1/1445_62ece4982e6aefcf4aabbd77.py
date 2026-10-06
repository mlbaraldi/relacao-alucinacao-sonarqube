def parse_frequency(frequency):
    import datetime
    """
    Given a frequency string with a number and a unit of time, return a corresponding
    datetime.timedelta instance or None if the frequency is None or "always".

    For instance, given "3 weeks", return datetime.timedelta(weeks=3)

    Raise ValueError if the given frequency cannot be parsed.
    """
    if frequency is None or frequency == "always":
        return None

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError("Invalid frequency format")

    number_str, unit = parts
    try:
        number = int(number_str)
    except ValueError:
        raise ValueError("Invalid number in frequency")

    allowed_units = {'weeks', 'days', 'hours', 'minutes', 'seconds'}
    if unit not in allowed_units:
        raise ValueError("Invalid unit in frequency")

    return datetime.timedelta(**{unit: number})
