
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]
    # Sort by length ascending, then alphabetically
    filtered.sort(key=lambda x: (len(x), x))
    return filtered
