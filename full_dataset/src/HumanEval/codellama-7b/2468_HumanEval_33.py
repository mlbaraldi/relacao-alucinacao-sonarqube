

def sort_third(l: list):
    l_sorted = sorted(l)
    l_sorted_third = []
    for i in range(0, len(l), 3):
        l_sorted_third.append(l_sorted[i])
    for i in range(1, len(l), 3):
        l_sorted_third.append(l[i])
    for i in range(2, len(l), 3):
        l_sorted_third.append(l[i])
    return l_sorted_third
