def _dump_string(obj, dumper=None):
    import sys
    """
    Dump to a py2-unicode or py3-string
    """
    if dumper is not None:
        dumped = dumper(obj)
    else:
        if sys.version_info[0] < 3:
            # Default to unicode in Python 2
            dumped = unicode(obj)
        else:
            # Default to str in Python 3
            dumped = str(obj)
    
    # Ensure the result is the correct type
    if sys.version_info[0] < 3:
        # Python 2: target is unicode
        if isinstance(dumped, str):
            return dumped.decode('utf-8')
        else:
            return unicode(dumped)
    else:
        # Python 3: target is str
        if isinstance(dumped, bytes):
            return dumped.decode('utf-8')
        else:
            return str(dumped)
