

def get_parser_option_specs(self, command_name):
    # Get the command object for the specified command name
    command = self.get_command(command_name)

    # Get the list of all options for the command
    options = command.option_list

    # Return the list of options
    return options
