

def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.

    :param e: Any exception instance.
    :type e: Exception
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return: The exception readable string
    :rtype: str
    """
    # Initialize the output string
    output = ""

    # Get the exception type and message
    exception_type = type(e).__name__
    exception_message = str(e)

    # Add the exception type and message to the output string
    output += f"{exception_type}: {exception_message}\n"

    # Get the call stack
    call_stack = traceback.extract_stack()

    # Add the call stack to the output string
    output += "".join(traceback.format_list(call_stack))

    # Get the exception path
    exception_path = traceback.extract_tb(e.__traceback__)

    # Add the exception path to the output string
    output += "".join(traceback.format_list(exception_path))

    # Return the output string
    return output
