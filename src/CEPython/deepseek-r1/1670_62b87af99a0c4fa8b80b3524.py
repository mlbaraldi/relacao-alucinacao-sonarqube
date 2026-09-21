def is_run_el(obj):
    """
    Check if the object contains an executable method 'run'.
    """
    return hasattr(obj, 'run') and callable(obj.run)
