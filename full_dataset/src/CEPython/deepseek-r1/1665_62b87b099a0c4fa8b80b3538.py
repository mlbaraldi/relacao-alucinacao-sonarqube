def is_fill_request_el(obj):
    """
    Check if the object has both 'fill' and 'request' methods that are callable.
    """
    return (hasattr(obj, 'fill') and callable(obj.fill) and
            hasattr(obj, 'request') and callable(obj.request))
