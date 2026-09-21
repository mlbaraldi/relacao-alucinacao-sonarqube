

def _normalizeargs(sequence, output=None):
    if output is None:
        output = []

    for item in sequence:
        if isinstance(item, Declaration):
            output.extend(_normalizeargs(item.interfaces))
        elif isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        else:
            output.append(item)

    return output
