
def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    if all(key.islower() for key in keys):
        return True
    elif all(key.isupper() for key in keys):
        return True
    else:
        return False
