

def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: A list of strings representing the script commands.
    :param separator: The string used to separate the commands. Default is " && ".
    :return: A string containing the script in one line.
    """
    if not script or not all(isinstance(cmd, str) for cmd in script):
        raise ValueError("The script must be a non-empty list of strings.")
    
    return separator.join(script)

# Example usage:
