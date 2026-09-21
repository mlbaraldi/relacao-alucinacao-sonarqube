

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    # This is a dictionary that maps parser names to another dictionary.
    # The second dictionary maps argument names to their types.
    # You will need to fill this dictionary with your own data.
    type_dict = {
        'main': {'arg1': int, 'arg2': float},
        'virsh': {'arg1': str, 'arg2': bool},
        'ospd': {'arg1': list, 'arg2': dict},
        # Add more parsers here
    }

    # Get the dictionary that maps argument names to their types for the given parser
    arg_type_dict = type_dict.get(parser_name, {})

    # Iterate over the arguments in values_dict
    for arg, value in values_dict.items():
        # Get the type for this argument
        arg_type = arg_type_dict.get(arg)

        # If a type was found, cast the value to this type
        if arg_type is not None:
            try:
                values_dict[arg] = arg_type(value)
            except ValueError:
                print(f"Error: Could not convert {value} to {arg_type}")

    return values_dict
