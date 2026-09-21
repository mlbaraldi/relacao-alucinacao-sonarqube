

def max_element(l: list):
    if not l:
        return None
    max_val = l[0]
    for i in l:
        if i > max_val:
            max_val = i
    return max_val
