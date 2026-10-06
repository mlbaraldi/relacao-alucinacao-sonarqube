

def difference(d1, d2, level=-1):
    result = {}
    for key, value in d1.items():
        if key not in d2:
            result[key] = value
        elif level == 1 and key in d2 and value != d2[key]:
            result[key] = value
        elif level > 1:
            result[key] = difference(value, d2[key], level-1)
    return result
