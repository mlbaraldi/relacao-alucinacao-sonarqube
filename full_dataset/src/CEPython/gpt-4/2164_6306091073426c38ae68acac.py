

def dict_insert(dic, val, key, *keys):
    if keys:  # if there are more keys
        if key not in dic:  # if key is not in dictionary
            dic[key] = {}  # create a new dictionary for this key
        dict_insert(dic[key], val, *keys)  # recursive call with the rest of keys
    else:  # if this is the last key
        dic[key] = val  # insert the value
