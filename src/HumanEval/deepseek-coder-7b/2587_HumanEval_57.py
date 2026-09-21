

def monotonic(l: list):
    if len(l) < 2:
        return True
    else:
        increasing = decreasing = True
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                decreasing = False
            if l[i] > l[i + 1]:
                increasing = False
        return increasing or decreasing

# Test cases
