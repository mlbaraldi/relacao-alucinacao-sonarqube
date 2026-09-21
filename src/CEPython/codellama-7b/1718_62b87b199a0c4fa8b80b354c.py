

def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (list, tuple)):
        return seq, type(seq)
    elif isinstance(seq, str):
        return seq.split(), str
    elif isinstance(seq, bytes):
        return seq.decode(), str
    else:
        raise TypeError("Unsupported sequence type: " + str(type(seq)))
