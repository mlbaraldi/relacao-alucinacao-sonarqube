

def _convert_non_cli_args(self, parser_name, values_dict):
    # Get the parser for the given command
    parser = self.get_parser(parser_name)

    # Iterate over the arguments in the values_dict
    for arg, value in values_dict.items():
        # Check if the argument is a flag
        if parser.has_option(arg):
            # Get the type of the argument
            arg_type = parser.get_option(arg).type

            # Convert the value to the correct type
            if arg_type == int:
                values_dict[arg] = int(value)
            elif arg_type == float:
                values_dict[arg] = float(value)
            elif arg_type == bool:
                values_dict[arg] = value.lower() == "true"
            else:
                values_dict[arg] = value
        else:
            # If the argument is not a flag, just leave it as a string
            values_dict[arg] = value

    return values_dict
