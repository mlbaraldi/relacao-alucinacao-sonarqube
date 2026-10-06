

def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: The script to convert to one line command.
    :param seperator: The separator to use between commands. Default is " && ".
    :return: The script as a one line command.
    """
    return seperator.join(script.split())
