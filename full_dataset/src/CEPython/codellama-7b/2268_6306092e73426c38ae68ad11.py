

def merge_extra_vars(vars_dict, extra_vars=None):
    if extra_vars is None:
        extra_vars = []
    for var in extra_vars:
        vars_dict[var] = True
    return vars_dict
