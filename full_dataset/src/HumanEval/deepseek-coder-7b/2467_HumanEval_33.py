

def sort_third(l: list):
    third_indices = [i for i in range(len(l)) if (i+1) % 3 == 0]
    third_values = sorted([l[i] for i in third_indices])
    for i, value in zip(third_indices, third_values):
        l[i] = value
    return l
