

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the elements
    s = set()

    # Iterate over the list
    for num in l:
        # If the negative of the current number is in the set, return True
        if -num in s:
            return True
        # Otherwise, add the number to the set
        s.add(num)

    # If no pair is found, return False
    return False
