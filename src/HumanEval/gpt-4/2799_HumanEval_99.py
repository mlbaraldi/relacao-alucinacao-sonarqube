
def closest_integer(value):
    num = float(value)
    if num >= 0:
        return int(num) if num - int(num) < 0.5 else int(num) + 1
    else:
        return int(num) if int(num) - num < 0.5 else int(num) - 1
