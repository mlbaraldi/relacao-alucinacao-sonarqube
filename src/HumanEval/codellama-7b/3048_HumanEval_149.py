
def sorted_list_sum(lst):
    # Remove strings with odd lengths from the list
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    lst.sort(key=lambda word: (len(word), word))
    
    return lst
