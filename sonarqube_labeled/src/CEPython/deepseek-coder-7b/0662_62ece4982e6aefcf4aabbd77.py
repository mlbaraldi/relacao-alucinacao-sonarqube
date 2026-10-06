import datetime


def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "always":
        return None

    try:
        number = int(frequency[:-1])
        unit = frequency[-1].lower()

        if unit == 's':
            return datetime.timedelta(seconds=number)
        elif unit == 'm':
            return datetime.timedelta(minutes=number)
        elif unit == 'h':
            return datetime.timedelta(hours=number)
        elif unit == 'd':
            return datetime.timedelta(days=number)
        elif unit == 'w':
            return datetime.timedelta(weeks=number)
        else:
            raise ValueError("Invalid unit of time")
    except ValueError:
        raise ValueError("Invalid frequency format")
