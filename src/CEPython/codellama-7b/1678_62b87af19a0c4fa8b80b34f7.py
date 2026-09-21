

def difference(d1, d2, level=-1):
    result = {}
    for key, value in d1.items():
        if key not in d2 or (key in d2 and d2[key] != value):
            result[key] = value
    if level > 0:
        for key, value in d1.items():
            if isinstance(value, dict):
                result[key] = difference(value, d2[key] if key in d2 else {}, level-1)
    return result
