import copy


def difference(d1, d2, level=-1):
    diff = {}
    for key in d1:
        if key not in d2:
            diff[key] = d1[key]
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if level != 1:
                sub_diff = difference(d1[key], d2[key], level)
                if sub_diff:
                    diff[key] = copy.deepcopy(sub_diff)
