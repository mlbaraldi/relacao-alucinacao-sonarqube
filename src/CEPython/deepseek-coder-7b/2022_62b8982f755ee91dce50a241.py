from dateutil.relativedelta import relativedelta


def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> MyRelativedelta(days=1.5, hours=2).normalized()
    MyRelativedelta(days=+1, hours=+2)

    :return:
        Returns a `MyRelativedelta` object with integer values for days and hours.
    """
    # Round the days and hours to the nearest integer
    normalized_days = round(self.days)
    normalized_hours = round(self.hours)
    
    # Create a new MyRelativedelta object with the normalized values
    return MyRelativedelta(days=normalized_days, hours=normalized_hours)
