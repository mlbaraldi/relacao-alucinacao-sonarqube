

def is_fill_request_el(obj):
    """
    Object contains executable methods 'fill' and 'request'.
    """
    if hasattr(obj, 'fill') and hasattr(obj, 'request'):
        if callable(getattr(obj, 'fill')) and callable(getattr(obj, 'request')):
            return True
    return False

# Test the function
