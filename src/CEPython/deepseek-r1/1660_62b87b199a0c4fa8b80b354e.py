def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Check if the sequence is a Source sequence
    if isinstance(seq, Source):
        return False
    # Check if the sequence itself is a FillRequest element
    if isinstance(seq, FillRequest):
        return True
    # Check if any element in the sequence is a FillRequest
    try:
        return any(isinstance(element, FillRequest) for element in seq)
    except TypeError:
        # The sequence is not iterable (e.g., a single non-sequence element)
        return False
