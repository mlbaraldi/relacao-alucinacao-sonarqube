
def next_smallest(lst):
    unique = sorted(set(lst))
    if len(unique) < 2:
        return None
    return unique[1]
