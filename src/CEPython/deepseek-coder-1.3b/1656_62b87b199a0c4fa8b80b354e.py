

def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    if not isinstance(seq, list):
        return False
    for element in seq:
        if not isinstance(element, FillRequest):
            return False
        if element.source:
            return False
    return True
