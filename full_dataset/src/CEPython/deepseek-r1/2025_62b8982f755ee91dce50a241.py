def normalized(self):
    import math
    from dateutil.relativedelta import relativedelta
    # Process each relative attribute from largest to smallest unit
    years = self.years
    months = self.months
    days = self.days
    hours = self.hours
    minutes = self.minutes
    seconds = self.seconds
    microseconds = self.microseconds

    # Process years to months
    frac_years, int_years = math.modf(years)
    months += frac_years * 12
    years = int(int_years)

    # Process months to days
    frac_months, int_months = math.modf(months)
    days += frac_months * 30  # assuming 30 days per month
    months = int(int_months)

    # Process days to hours
    frac_days, int_days = math.modf(days)
    hours += frac_days * 24
    days = int(int_days)

    # Process hours to minutes
    frac_hours, int_hours = math.modf(hours)
    minutes += frac_hours * 60
    hours = int(int_hours)

    # Process minutes to seconds
    frac_minutes, int_minutes = math.modf(minutes)
    seconds += frac_minutes * 60
    minutes = int(int_minutes)

    # Process seconds to microseconds
    frac_seconds, int_seconds = math.modf(seconds)
    microseconds += frac_seconds * 1e6
    seconds = int(int_seconds)

    # Process microseconds (truncate any remaining fractional part)
    frac_micro, int_micro = math.modf(microseconds)
    microseconds = int(int_micro)

    # Collect absolute parameters
    absolute_params = {}
    for attr in ['year', 'month', 'day', 'weekday', 'yearday', 'nlyearday',
                 'hour', 'minute', 'second', 'microsecond']:
        value = getattr(self, attr, None)
        if value is not None:
            absolute_params[attr] = value

    # Collect relative parameters
    relative_params = {
        'years': years,
        'months': months,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'microseconds': microseconds,
        'leapdays': self.leapdays,
    }

    # Combine all parameters and create new relativedelta
    combined = {**absolute_params, **relative_params}
    return relativedelta(**combined)

# Attach the normalized method to the relativedelta class (if necessary)
