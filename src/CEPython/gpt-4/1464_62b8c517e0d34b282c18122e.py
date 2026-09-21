import traceback


def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.
    :param e: Any exception instance.
    :type e: Exception
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return The exception readable string
    :rtype str
    """
    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__, limit=max_level)

    # Format the traceback
    tb_str = []
    for filename, line, func, text in tb:
        # Limit the path level
        path = filename.split('/')
        if len(path) > max_path_level:
            filename = '.../' + '/'.join(path[-max_path_level:])
        tb_str.append(f'  File "{filename}", line {line}, in {func}\n    {text}')

    # Format the exception
    return f'{e.__class__.__name__}: {e}\n' + '\n'.join(tb_str)
