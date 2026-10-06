

def dict_insert(dic, val, key, *keys):
    if not keys:
        dic[key] = val
        return

    if key not in dic:
        dic[key] = {}

    dict_insert(dic[key], val, *keys)
