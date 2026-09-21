

def _get_seq_with_type(seq, bufsize=None):
    """
    Return a (sequence, type) pair.
    Sequence is derived from *seq*
    (or is *seq*, if that is of a sequence type).
    """
    sequence = seq
    seq_type = type(seq)

    # If seq is not a sequence, we create a new one
    if not isinstance(seq, (list, tuple, str)):
        sequence = []
        if seq_type is int:
            sequence = [0] * bufsize
        elif seq_type is float:
            sequence = [0.0] * bufsize
        elif seq_type is str:
            sequence = [''] * bufsize

    return sequence, seq_type
