

def get_option_spec(self, command_name, argument_name):
    # Get the command object for the specified command name
    command = self.get_command(command_name)

    # Get the argument object for the specified argument name
    argument = command.get_argument(argument_name)

    # Return the option specification for the argument
    return argument.get_option_spec()
