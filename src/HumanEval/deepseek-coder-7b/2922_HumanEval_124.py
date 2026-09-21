
def valid_date(date):
    try:
        datetime.strptime(date, '%m-%d-%Y')
        return True
    except ValueError:
        return False
