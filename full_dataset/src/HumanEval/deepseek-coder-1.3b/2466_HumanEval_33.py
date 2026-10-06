

def sort_third(l: list):
    third_elements = sorted([l[i] for i in range(len(l)) if (i+1) % 3 == 0])
    for i in range(len(l)):
        if (i+1) % 3 == 0:
            l[i] = third_elements.pop(0)
    return l
