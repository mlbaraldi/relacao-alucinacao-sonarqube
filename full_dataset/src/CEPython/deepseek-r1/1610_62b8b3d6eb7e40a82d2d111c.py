def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarations, tuples, or single
    interfaces.

    Anything but individual interfaces or implements specs will be expanded.
    """
    if output is None:
        output = []
    for item in sequence:
        if isinstance(item, tuple):
            _normalizeargs(item, output)
        elif isinstance(item, Declaration):
            _normalizeargs(item.declarations, output)
        else:
            output.append(item)
    return output

# Assume Declaration is a class with a 'declarations' attribute for the sake of this example
