

def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True
    # Check for non-decreasing
    is_increasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            is_increasing = False
            break
    # Check for non-increasing
    is_decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            is_decreasing = False
            break
    return is_increasing or is_decreasing
