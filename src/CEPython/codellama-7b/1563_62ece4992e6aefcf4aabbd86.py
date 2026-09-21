

def _dump_string(obj, dumper=None):
    if dumper is None:
        dumper = lambda x: x
    return dumper(obj)
