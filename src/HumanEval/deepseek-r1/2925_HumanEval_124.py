
def valid_date(date):
    """Validates a given date string in the format mm-dd-yyyy."""
    if not date:
        return False
    
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month_str, day_str, year_str = parts
    
    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        return False
    
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False
    
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)  # Year is validated by length and being digits
    
    if month < 1 or month > 12:
        return False
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= day <= 31):
            return False
    elif month in {4, 6, 9, 11}:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False
    
    return True
