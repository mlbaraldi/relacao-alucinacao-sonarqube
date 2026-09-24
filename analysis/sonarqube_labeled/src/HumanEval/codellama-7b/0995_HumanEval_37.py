

def sort_even(l: list):
    l_even = [l[i] for i in range(0, len(l), 2)]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_even.sort()
    l_odd.sort()
    return [l_even, l_odd]
