

def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if isinstance(obj, str):
        return obj
    else:
        return str(obj)
