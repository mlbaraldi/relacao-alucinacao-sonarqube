

def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    try:
        return self.commands[command_name][argument_name]
    except KeyError:
        return None
