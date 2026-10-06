

def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is None:
        # Python 2
        if isinstance(obj, str):
            return obj
        # Python 3
        elif isinstance(obj, str):
            return obj.encode('utf-8')
    else:
        # Python 2
        if isinstance(obj, str):
            return obj
        # Python 3
        elif isinstance(obj, str):
            return obj.encode('utf-8')
