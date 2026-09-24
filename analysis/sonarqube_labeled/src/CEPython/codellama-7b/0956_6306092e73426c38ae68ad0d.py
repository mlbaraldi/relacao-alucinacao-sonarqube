

def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
    # Create a new instance of the complex type
    complex_type = ComplexType(type_name, option_name, spec_option)

    # Add the subcommand to the complex type
    complex_type.subcommands.append(subcommand)

    # Return the complex type instance
    return complex_type
