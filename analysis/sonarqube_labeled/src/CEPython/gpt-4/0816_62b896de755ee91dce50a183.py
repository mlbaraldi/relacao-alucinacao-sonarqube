from datetime import datetime


def parse(self, timestr, default=None,
              ignoretz=False, tzinfos=None, **kwargs):
    # If default is provided and is a datetime object, use it as the base
    if default and isinstance(default, datetime):
        dt = default
    else:
        dt = datetime.now()

    # Try to parse the string using strptime
    try:
        dt = datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        # If strptime fails, try to parse the string manually
        parts = timestr.split()
        if len(parts) == 2:
            date, time = parts
            year, month, day = map(int, date.split('-'))
            hour, minute, second = map(int, time.split(':'))
            dt = datetime(year, month, day, hour, minute, second)

    # If ignoretz is True, return a naive datetime object
    if ignoretz:
        dt = dt.replace(tzinfo=None)

    return dt
