
def next_smallest(lst):
    if len(lst) < 2:
        return None
    min1 = min(lst)
    lst.remove(min1)
    min2 = min(lst)
    lst.append(min1)
    return min2
