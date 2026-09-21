
def sorted_list_sum(lst):
    # Filter out the strings with odd lengths
    lst = [i for i in lst if len(i) % 2 == 0]
    # Sort the list by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
