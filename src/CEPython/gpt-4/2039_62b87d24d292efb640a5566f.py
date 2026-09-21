

def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == 'uppercase':
        return [piece.upper() for piece in pieces]
    elif style == 'lowercase':
        return [piece.lower() for piece in pieces]
    else:
        return "Invalid style"
