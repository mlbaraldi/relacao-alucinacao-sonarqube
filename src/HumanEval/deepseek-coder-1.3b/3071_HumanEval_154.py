
def cycpattern_check(a , b):
    # Check if b is a substring of a
    if b in a:
        return True

    # Check if b is a rotation of a
    for i in range(len(b)):
        if b in a[i:] + a[:i]:
            return True

    # If none of the above conditions are met, return False
    return False
