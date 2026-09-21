
def sort_array(array):
    """
    Returns a sorted copy of the input array based on the sum of the first and last elements.
    The sorting order is ascending if the sum is odd, and descending if the sum is even.
    """
    if len(array) <= 1:
        return list(array)
    first = array[0]
    last = array[-1]
    sum_fl = first + last
    if sum_fl % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
