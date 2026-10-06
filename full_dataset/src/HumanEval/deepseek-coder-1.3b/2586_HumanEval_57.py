

def monotonic(l: list):
    if len(l) < 2:
        return True
    else:
        diff = [l[i+1] - l[i] for i in range(len(l) - 1)]
        if all(x > 0 for x in diff):
            return True
        elif all(x < 0 for x in diff):
            return True
        else:
            return False
