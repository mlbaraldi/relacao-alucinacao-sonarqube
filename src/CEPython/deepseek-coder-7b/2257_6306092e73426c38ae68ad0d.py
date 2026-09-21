

def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
    """
    Build the complex argument type

    :param subcommand: the command name
    :param type_name: the complex type name
    :param option_name: the option name
    :param spec_option: option's specifications
    :return: the complex type instance
    """
    return ComplexArgument(subcommand, type_name, option_name, spec_option)

# Example usage:
