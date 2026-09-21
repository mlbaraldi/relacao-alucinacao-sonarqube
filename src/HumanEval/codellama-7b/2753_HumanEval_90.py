
def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst)
    for i in range(1, len(lst)):
        if sorted_lst[i] != sorted_lst[i-1]:
            return sorted_lst[i]
    return None
