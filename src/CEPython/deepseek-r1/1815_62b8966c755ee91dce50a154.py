def isoparse(self, dt_str):
    import re
    from datetime import datetime, timedelta, date
    from dateutil import tz
    if 'T' in dt_str:
        date_part, time_part = dt_str.split('T', 1)
    else:
        date_part = dt_str
        time_part = ''
    if 'W' in date_part.upper() and 'W' in date_part:
        week_date = parse_week_date(date_part)
        parsed_date = {
            'type': 'week',
            'year': week_date['year'],
            'week': week_date['week'],
            'day': week_date['day'],
            'complete': week_date['day'] != 0,
        }
        date_obj = iso_to_gregorian(week_date['year'], week_date['week'], week_date['day'])
    else:
        regular_date = parse_regular_date(date_part)
        parsed_date = {
            'type': 'regular',
            'year': regular_date['year'],
            'month': regular_date['month'],
            'day': regular_date['day'],
            'complete': regular_date['has_day'],
        }
        date_obj = date(regular_date['year'], regular_date['month'], regular_date['day'])
    if time_part and not parsed_date['complete']:
        raise ValueError("Incomplete date cannot be combined with time")
    tz_info = None
    parsed_time = {'hours': 0, 'minutes': 0, 'seconds': 0, 'microseconds': 0, 'add_day': False}
    if time_part:
        tz_match = re.search(r'([Zz]|[+-]\d{2}(:?\d{2})?)$', time_part)
        if tz_match:
            tz_start = tz_match.start()
            time_str_part = time_part[:tz_start]
            tz_str_part = tz_match.group().upper()
        else:
            time_str_part = time_part
            tz_str_part = ''
        parsed_time = parse_time(time_str_part)
        tz_info = parse_timezone(tz_str_part)
    else:
        parsed_time = {'hours': 0, 'minutes': 0, 'seconds': 0, 'microseconds': 0, 'add_day': False}
    if parsed_time['add_day']:
        date_obj += timedelta(days=1)
    naive_dt = datetime(
        date_obj.year, date_obj.month, date_obj.day,
        parsed_time['hours'], parsed_time['minutes'], parsed_time['seconds'],
        parsed_time['microseconds']
    )
    if tz_info:
        aware_dt = naive_dt.replace(tzinfo=tz_info)
    else:
        aware_dt = naive_dt
    return aware_dt
