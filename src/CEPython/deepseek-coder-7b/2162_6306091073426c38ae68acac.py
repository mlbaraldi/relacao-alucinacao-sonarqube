

def dict_insert(dic, val, key, *keys):
    """
    Insert a value of a nested key into a dictionary.

    To insert value for a nested key, all ancestor keys should be given as
    method's arguments.

    Example:
      dict_insert({}, 'val', 'key1.key2'.split('.'))

    :param dic: a dictionary object to insert the nested key value into
    :param val: a value to insert to the given dictionary
    :param key: first key in a chain of key that will store the value
    :param keys: sub keys in the keys chain
    """
    # Split the key by '.' to get the nested keys
    keys = key.split('.') + list(keys)

    # Traverse the dictionary to insert the value
    for k in keys[:-1]:
        dic = dic.setdefault(k, {})

    # Insert the value at the last key
    dic[keys[-1]] = val

# Example usage:
