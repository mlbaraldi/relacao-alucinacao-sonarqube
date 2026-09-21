def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback
    import os
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
    tb = e.__traceback__
    if tb is None:
        return f"{type(e).__name__}: {str(e)}"
    
    frames = traceback.extract_tb(tb, limit=max_level)
    processed_frames = []
    
    for frame in frames:
        filename = frame.filename
        parts = filename.split(os.path.sep)
        if len(parts) > max_path_level:
            parts = parts[-max_path_level:]
        truncated_filename = os.path.sep.join(parts)
        processed_frame = traceback.FrameSummary(
            truncated_filename,
            frame.lineno,
            frame.name,
            line=frame.line
        )
        processed_frames.append(processed_frame)
    
    formatted_frames = traceback.format_list(processed_frames)
    exception_lines = traceback.format_exception_only(type(e), e)
    
    result = ["Traceback (most recent call last):\n"]
    result.extend(formatted_frames)
    result.extend(exception_lines)
    return ''.join(result).strip()
