

def _get_seq_with_type(seq, bufsize=None):
    """
    Return a (sequence, type) pair.
    Sequence is derived from *seq*
    (or is *seq*, if that is of a sequence type).
    """
    sequence = seq if isinstance(seq, (list, tuple, str)) else str(seq)
    sequence_type = type(sequence)
    return sequence, sequence_type
