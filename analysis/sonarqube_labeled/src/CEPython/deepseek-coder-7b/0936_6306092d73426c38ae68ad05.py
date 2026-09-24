

def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    if command_name in self.options and argument_name in self.options[command_name]:
        return self.options[command_name][argument_name]
    else:
        return None
