
def valid_date(date):
    try:
        # Check if the date string is not empty
        if not date:
            return False

        # Check if the date string is in the correct format
        if len(date.split('-')) != 3:
            return False

        # Split the date string into month, day, and year
        month, day, year = map(int, date.split('-'))

        # Check if the month is not less than 1 or higher than 12
        if month < 1 or month > 12:
            return False

        # Check if the day is not less than 1 or higher than the number of days in the month
        if day < 1 or day > 31:
            return False

        # Check if the year is not less than 1 or higher than the current year
        if year < 1 or year > datetime.now().year:
            return False

        # If the date is valid, return True
        return True

    except ValueError:
        # If the date string is not in the correct format, return False
        return False
