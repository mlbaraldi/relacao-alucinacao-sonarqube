
def cycpattern_check(a , b):
    # Check if b is a substring of a
    if b in a:
        return True
    # Check if any rotation of b is a substring of a
    for i in range(len(b)):
        if a.find(b[i:]+b[:i]) != -1:
            return True
    return False
