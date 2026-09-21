

def sort_even(l: list):
    even_indices = [x for i, x in enumerate(l) if i % 2 == 0]
    even_indices.sort()
    for i, x in enumerate(l):
        if i % 2 == 0:
            l[i] = even_indices.pop(0)
    return l
