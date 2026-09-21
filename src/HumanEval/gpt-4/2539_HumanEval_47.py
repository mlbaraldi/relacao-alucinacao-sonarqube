

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    n = len(l)
    m = n - 1
    if (n % 2):
        return l[int((m)/2)]
    else:
        return (l[int(m/2)] + l[int((m/2) + 1)]) / 2.0
