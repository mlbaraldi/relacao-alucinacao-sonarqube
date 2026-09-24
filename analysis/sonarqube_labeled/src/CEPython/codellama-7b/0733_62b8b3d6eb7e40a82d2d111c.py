

def _normalizeargs(sequence, output=None):
    if output is None:
        output = []
    for item in sequence:
        if isinstance(item, Declaration):
            output.append(item)
        elif isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif isinstance(item, Interface):
            output.append(item)
        else:
            raise TypeError("Unsupported type: " + str(type(item)))
    return output
