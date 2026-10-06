import copy


def difference(d1, d2, level=-1):
    if level == 0:
        return {}
    diff = {}
    for key in d1:
        if key not in d2:
            diff[key] = copy.deepcopy(d1[key])
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            nested_diff = difference(d1[key], d2[key], level - 1)
            if nested_diff:
                diff[key] = nested_diff
        elif d1[key] != d2[key]:
            diff[key] = d1[key]
    return diff
