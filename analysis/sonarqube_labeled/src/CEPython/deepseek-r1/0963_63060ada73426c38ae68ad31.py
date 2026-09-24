def _convert_non_cli_args(self, parser_name, values_dict):
    import argparse
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    # Retrieve the parser for the given parser_name
    parser = self._get_parser(parser_name)  # Assume this method exists to get the parser

    for key in list(values_dict.keys()):
        value = values_dict[key]
        # Find the corresponding action in the parser
        action = None
        for a in parser._actions:
            if a.dest == key:
                action = a
                break
        if not action:
            continue  # No action found for this key, skip conversion

        # Handle boolean actions (store_true/store_false)
        if isinstance(action, (argparse._StoreTrueAction, argparse._StoreFalseAction)):
            # Convert string to boolean based on common representations
            try:
                str_val = str(value).lower()
                if str_val in {'true', 'yes', '1', 'on'}:
                    converted = True
                elif str_val in {'false', 'no', '0', 'off'}:
                    converted = False
                else:
                    # If the string is not recognized, default to boolean conversion
                    converted = bool(value)
            except AttributeError:
                # If value is not a string (unlikely), use its boolean value
                converted = bool(value)
            values_dict[key] = converted
        elif action.type is not None:
            # Convert using the action's type converter
            try:
                converted = action.type(value)
                values_dict[key] = converted
            except (TypeError, ValueError):
                # If conversion fails, leave as string or handle error as needed
                pass
        # If no type is specified and not a boolean action, leave as string
