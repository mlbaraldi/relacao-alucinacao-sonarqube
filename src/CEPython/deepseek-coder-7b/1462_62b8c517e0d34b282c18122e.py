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
    :return: The exception readable string
    :rtype: str
    """
    # Get the exception's type, value, and traceback
    exception_type, exception_value, exception_traceback = cls.exc_info()
    
    # Format the exception's type and value
    exception_str = f"{exception_type.__name__}: {exception_value}"
    
    # Format the traceback
    tb_frames = traceback.extract_tb(exception_traceback)
    formatted_traceback = []
    for i, frame in enumerate(tb_frames):
        if i >= max_level:
            break
        if frame.lineno is not None and frame.lineno <= max_path_level:
            formatted_traceback.append(f"{frame.filename}:{frame.lineno} in {frame.name}")
        else:
            formatted_traceback.append(f"{frame.filename} in {frame.name}")
    
    # Combine the exception string and the formatted traceback
    exception_str += "\nTraceback (most recent call last):\n" + "\n".join(formatted_traceback)
    
    return exception_str

# Example usage:
