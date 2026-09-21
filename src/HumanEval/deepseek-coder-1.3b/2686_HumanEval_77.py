
def iscube(a):
    if a < 0:
        return False
    n = round(a ** (1. / 3))
    return n ** 3 == a
