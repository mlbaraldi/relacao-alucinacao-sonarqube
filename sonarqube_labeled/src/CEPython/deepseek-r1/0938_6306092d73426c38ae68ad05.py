def get_option_spec(self, command_name, argument_name):
    import click
    """
    Gets the specification for the specified option name.
    """
    # Retrieve the command object from the group's commands dictionary
    command = self.commands.get(command_name)
    if not command:
        return None
    
    # Iterate through each parameter in the command
    for param in command.params:
        # Check if the parameter is an Option and if its name matches
        if isinstance(param, click.Option) and param.name == argument_name:
            return param
    
    # Return None if no matching option is found
    return None
