

def _dictsum(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k not in result:
                result[k] = v
            else:
                result[k] += v
    return result
