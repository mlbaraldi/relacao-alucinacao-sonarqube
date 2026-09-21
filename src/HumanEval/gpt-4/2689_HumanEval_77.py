
def iscube(a):
    cube_root = round(abs(a) ** (1. / 3))
    return cube_root ** 3 == abs(a)
