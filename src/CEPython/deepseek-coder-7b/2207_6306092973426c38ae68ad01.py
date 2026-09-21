

def get_deprecated_args(self):
    """
    Returning dict with options which deprecate others.
    """
    deprecated_options = {}
    for option, deprecated_options_list in self.options.items():
        if deprecated_options_list:
            deprecated_options[option] = deprecated_options_list
    return deprecated_options
