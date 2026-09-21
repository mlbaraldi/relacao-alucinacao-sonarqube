
def match_parens(lst):
    # Concatenate the strings in both possible orders
    str1 = lst[0] + lst[1]
    str2 = lst[1] + lst[0]

    # Check if either concatenated string is good
    if is_good(str1) or is_good(str2):
        return 'Yes'
    else:
        return 'No'

