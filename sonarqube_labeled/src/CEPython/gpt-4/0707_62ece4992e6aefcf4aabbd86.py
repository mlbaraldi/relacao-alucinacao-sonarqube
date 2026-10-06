import sys


def _dump_string(obj, dumper=None):
    """
    Dump to a py2-unicode or py3-string
    """
    if sys.version_info[0] == 2:
        if isinstance(obj, str):
            return obj.decode('utf-8')
        elif isinstance(obj, unicode):
            return obj
        else:
            return unicode(obj)
    else:
        return str(obj)
