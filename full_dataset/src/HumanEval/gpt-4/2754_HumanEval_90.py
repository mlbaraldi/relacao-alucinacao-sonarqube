
def next_smallest(lst):
    # Remove duplicates from the list
    lst = list(set(lst))
    # Sort the list in ascending order
    lst.sort()
    # If the list has less than 2 elements, return None
    if len(lst) < 2:
        return None
    # Otherwise, return the second element
    else:
        return lst[1]
