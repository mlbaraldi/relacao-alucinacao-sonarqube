

def monotonic(l: list):
    if len(l) < 2:
        return True
    is_increasing = l[1] > l[0]
    for i in range(2, len(l)):
        if (l[i] > l[i-1]) != is_increasing:
            return False
    return True
