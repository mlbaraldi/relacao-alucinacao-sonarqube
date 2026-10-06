
def closest_integer(value):
    value = float(value)
    if value >= 0:
        return int(value) if value - int(value) < 0.5 else int(value) + 1
    else:
        return int(value) if abs(value - int(value)) < 0.5 else int(value) - 1

