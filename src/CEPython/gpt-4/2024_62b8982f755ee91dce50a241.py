from dateutil.relativedelta import relativedelta
import math


def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Returns a :class:`dateutil.relativedelta.relativedelta` object.
    """
    # Calculate the integer and fractional part of the days
    days_int = math.floor(self.days)
    days_frac = self.days - days_int

    # Convert the fractional part of the days into hours and add it to the hours
    hours = self.hours + days_frac * 24

    # Return a new relativedelta object with the normalized values
    return relativedelta(days=days_int, hours=int(hours))
