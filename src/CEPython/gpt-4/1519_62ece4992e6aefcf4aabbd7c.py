

def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: The script to be converted
    :param seperator: The separator to be used between commands
    :return: The script converted to a one line command
    """
    # Split the script into lines
    lines = script.split('\n')
    # Remove any empty lines
    lines = [line for line in lines if line.strip() != '']
    # Join the lines with the separator and return
    return seperator.join(lines)
