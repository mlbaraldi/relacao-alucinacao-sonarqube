

def pairs_sum_to_zero(l):
    """
    This function checks if there are two distinct elements in the list that sum to zero.
    """
    if len(l) < 2:
        return False
    
    # Check if there are at least two zeros
    zero_count = l.count(0)
    if zero_count >= 2:
        return True
    
    # Create a set of elements for O(1) lookups
    elements = set(l)
    
    # Check each element for the presence of its negative
    for num in l:
        if num != 0 and -num in elements:
            return True
    
    return False
