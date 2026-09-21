
def choose_num(x, y):
    if x % 2 == 0:
        return x
    if y % 2 == 0:
        return y
    for i in range(x, y+1, 2):
        if i % 2 == 0:
            return i
    return -1
