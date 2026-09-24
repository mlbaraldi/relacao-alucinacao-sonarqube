
def check_dict_case(dict):
    if not dictionary:
        return False

    keys = dictionary.keys()
    all_lower = all(k.islower() for k in keys)
    all_upper = all(k.isupper() for k in keys)

    return all_lower or all_upper
