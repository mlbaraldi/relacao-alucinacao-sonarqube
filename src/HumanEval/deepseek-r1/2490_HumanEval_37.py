

def sort_even(l: list):
    even_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    sorted_evens = sorted(even_elements)
    res = []
    k = 0
    for i in range(len(l)):
        if i % 2 == 0:
            res.append(sorted_evens[k])
            k += 1
        else:
            res.append(l[i])
    return res
