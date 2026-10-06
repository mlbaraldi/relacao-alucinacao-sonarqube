

def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest is a class with a specific identifier or attribute
    # and Source is a class with a specific identifier or attribute
    # We need to define these classes and their attributes for a precise implementation

    # For the purpose of this example, let's assume:
    # - FillRequest is a class with a specific attribute 'fill_request'
    # - Source is a class with a specific attribute 'source'
    # - A Source sequence is a sequence that does not have the 'fill_request' attribute

    # Check if seq is a FillRequest element
    if hasattr(seq, 'fill_request'):
        return True

    # Check if seq contains at least one FillRequest element
    if any(hasattr(item, 'fill_request') for item in seq):
        return True

    # Check if seq is not a Source sequence
    if not any(hasattr(item, 'source') for item in seq):
        return True

    # If none of the conditions are met, return False
    return False

# Example usage:
# Assuming FillRequest and Source are classes with specific attributes
# fill_request_seq = FillRequest()
# source_seq = Source()
# seq = [fill_request_seq, source_seq, [fill_request_seq, source_seq]]

# print(is_fill_request_seq(seq))  # Should return True
