from dateutil.relativedelta import relativedelta


def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> MyClass(1.5, 2).normalized()
    MyClass(1, 14)

    :return:
        Returns a `dateutil.relativedelta.relativedelta` object.
    """
    return MyClass(int(self.days), int(self.hours))
