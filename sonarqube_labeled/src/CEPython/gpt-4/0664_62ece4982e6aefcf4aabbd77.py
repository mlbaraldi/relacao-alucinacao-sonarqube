import datetime


def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "always":
        return None

    try:
        number, unit = frequency.split()
        number = int(number)
    except ValueError:
        raise ValueError("Frequency cannot be parsed")

    if unit.endswith('s'):
        unit = unit[:-1]

    if unit == "week":
        return datetime.timedelta(weeks=number)
    elif unit == "day":
        return datetime.timedelta(days=number)
    elif unit == "hour":
        return datetime.timedelta(hours=number)
    elif unit == "minute":
        return datetime.timedelta(minutes=number)
    elif unit == "second":
        return datetime.timedelta(seconds=number)
    else:
        raise ValueError("Frequency cannot be parsed")
