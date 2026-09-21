
def strange_sort_list(lst):
    result = []
    working = list(lst)
    while working:
        # Take the minimum
        mn = min(working)
        result.append(mn)
        working.remove(mn)
        # Take the maximum if elements remain
        if working:
            mx = max(working)
            result.append(mx)
            working.remove(mx)
    return result
