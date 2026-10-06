

def is_fill_request_seq(seq):
    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, list):
        for item in seq:
            if is_fill_request_seq(item):
                return True
    return False
