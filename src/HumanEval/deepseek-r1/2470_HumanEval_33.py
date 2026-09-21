

def sort_third(l: list):
    # Extract elements at indices divisible by three
    to_sort = [elem for idx, elem in enumerate(l) if idx % 3 == 0]
    # Sort these elements
    sorted_elems = sorted(to_sort)
    # Create an iterator for the sorted elements
    iter_sorted = iter(sorted_elems)
    # Build the resulting list
    result = []
    for idx, elem in enumerate(l):
        if idx % 3 == 0:
            result.append(next(iter_sorted))
        else:
            result.append(elem)
    return result
