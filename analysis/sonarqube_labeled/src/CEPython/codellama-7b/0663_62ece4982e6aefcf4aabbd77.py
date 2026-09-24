import datetime


def parse_frequency(frequency):
    if frequency is None or frequency == "always":
        return None
    try:
        amount, unit = frequency.split()
        amount = int(amount)
        if unit == "week":
            unit = "weeks"
        elif unit == "day":
            unit = "days"
        elif unit == "hour":
            unit = "hours"
        elif unit == "minute":
            unit = "minutes"
        elif unit == "second":
            unit = "seconds"
        else:
            raise ValueError(f"Invalid unit: {unit}")
        return datetime.timedelta(**{unit: amount})
    except ValueError:
        raise ValueError(f"Invalid frequency: {frequency}")
