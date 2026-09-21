

def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """

    # Define the default type for each argument
    default_types = {
        'str': str,
        'int': int,
        'float': float,
        'bool': bool,
    }

    # Iterate over the arguments
    for arg_name, arg_value in values_dict.items():
        # Check if the argument type is defined
        arg_type = default_types.get(arg_value.type)
        if arg_type is not None:
            # Try to convert the argument to the defined type
            try:
                values_dict[arg_name] = arg_type(arg_value)
            except ValueError:
                # If the conversion fails, print an error message
                print(f"Error: Argument '{arg_name}' of type '{arg_value.type}' cannot be converted to '{arg_type.__name__}'")
