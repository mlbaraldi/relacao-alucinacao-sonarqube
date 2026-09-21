def _get_seq_with_type(seq, bufsize=None):
    from collections.abc import Sequence
    if isinstance(seq, Sequence):
        return (seq, type(seq))
    else:
        return ([seq], list)
