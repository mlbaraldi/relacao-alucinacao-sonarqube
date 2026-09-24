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
    tb = traceback.extract_tb(e.__traceback__, max_depth=max_path_level)
    formatted_traceback = []
    for i, (filename, line_no, function_name, text, lines) in enumerate(tb):
        if i < max_level:
            formatted_traceback.append(f'File "{filename}", line {line_no}, in {function_name}:\n{text}')
        else:
            break
    return '\n'.join(formatted_traceback)
