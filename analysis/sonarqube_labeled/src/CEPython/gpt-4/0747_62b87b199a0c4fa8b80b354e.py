

def is_fill_request_seq(seq):
    # Check if seq is a FillRequest element
    if isinstance(seq, FillRequest):
        return True

    # Check if seq is not a Source sequence
    if isinstance(seq, Source):
        return False

    # Check if seq contains at least one FillRequest element
    for element in seq:
        if isinstance(element, FillRequest):
            return True

    return False
