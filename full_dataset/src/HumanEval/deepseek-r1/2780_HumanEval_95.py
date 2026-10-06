
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not dct:
        return False
    
    # Check if all keys are strings
    for key in dct.keys():
        if not isinstance(key, str):
            return False
    
    # Check if all keys are lowercase or all are uppercase
    all_lower = True
    all_upper = True
    
    for key in dct.keys():
        if not key.islower():
            all_lower = False
        if not key.isupper():
            all_upper = False
    
    return all_lower or all_upper
