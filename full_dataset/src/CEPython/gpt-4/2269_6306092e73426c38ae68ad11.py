

def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend ``vars_dict`` with ``extra_vars``

    :param vars_dict: Dictionary to merge extra-vars into
    :param extra_vars: List of extra-vars
    """
    if extra_vars is None:
        return vars_dict

    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
        else:
            print(f"Warning: Ignored non-dict extra var: {var}")

    return vars_dict
