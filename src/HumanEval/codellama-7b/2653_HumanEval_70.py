
def strange_sort_list(lst):
    if len(lst) == 0:
        return []
    else:
        min_val = min(lst)
        max_val = max(lst)
        lst.remove(min_val)
        lst.remove(max_val)
        return [min_val, max_val] + strange_sort_list(lst)
