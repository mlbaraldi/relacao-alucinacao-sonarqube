

def is_fill_request_el(obj):
    """
    Object contains executable methods 'fill' and 'request'.
    """
    if not hasattr(obj, 'fill') or not callable(obj.fill):
        return False
    if not hasattr(obj, 'request') or not callable(obj.request):
        return False
    return True
