def difference(d1, d2, level=-1):
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
        else:
            v1 = d1[key]
            v2 = d2[key]
