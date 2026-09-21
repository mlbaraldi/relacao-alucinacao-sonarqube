

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            try:
                if '.' in value:
                    values_dict[key] = float(value)
                else:
                    values_dict[key] = int(value)
            except ValueError:
                pass  # Value cannot be converted to int or float, leave it as a string
        elif isinstance(value, bool):
            if value.lower() in ['true', 'false']:
                values_dict[key] = value.lower() == 'true'
            else:
                values_dict[key] = bool(value)
