

def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend `vars_dict` with `extra_vars`

    :param vars_dict: Dictionary to merge extra_vars into
    :param extra_vars: List of extra_vars
    """
    if extra_vars is not None:
        for var in extra_vars:
            if isinstance(var, dict):
                vars_dict.update(var)
            else:
                vars_dict[var] = None
    return vars_dict
