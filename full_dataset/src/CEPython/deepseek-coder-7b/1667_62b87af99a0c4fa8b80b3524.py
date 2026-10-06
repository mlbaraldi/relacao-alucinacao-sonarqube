

def is_run_el(obj):
    """
    Object contains executable method 'run'.
    """
    if hasattr(obj, 'run'):
        if callable(getattr(obj, 'run')):
            return True
    return False
