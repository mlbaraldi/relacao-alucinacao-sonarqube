from dateutil.relativedelta import relativedelta


def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "always":
        return None

    try:
        weeks, days, hours, minutes, seconds = map(int, frequency.split())
        return relativedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    except ValueError:
        raise ValueError(f"Invalid frequency string: {frequency}")
