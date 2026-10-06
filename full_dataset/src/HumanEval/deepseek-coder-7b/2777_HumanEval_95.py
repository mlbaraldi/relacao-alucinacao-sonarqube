
def check_dict_case(dict):
    if not dict:
        return False
    first_key = next(iter(dict))
    return all(isinstance(k, str) and k.islower() == first_key.islower() for k in dict)
