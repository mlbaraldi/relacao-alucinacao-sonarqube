

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 2:
        return False
    else:
        return any(x + y == 0 for x in l for y in l if x != y)

# Test cases
