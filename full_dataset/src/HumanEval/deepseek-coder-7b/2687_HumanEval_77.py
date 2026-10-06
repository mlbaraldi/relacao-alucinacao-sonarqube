
def iscube(a):
    if a < 0:
        a = -a
    root = round(math.pow(a, (1. / 3)))
    return root ** 3 == a
