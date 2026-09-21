from datetime import datetime


def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    """
    # Assuming the D* nodes expect the datetime in the format 'YYYY-MM-DD HH:MM:SS'
    return dt.strftime('%Y-%m-%d %H:%M:%S')

# Test the function
