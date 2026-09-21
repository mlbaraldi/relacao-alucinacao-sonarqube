

def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    rendered_pieces = []
    for piece in pieces:
        rendered_piece = piece
        for key, value in style.items():
            rendered_piece = rendered_piece.replace(key, value)
        rendered_pieces.append(rendered_piece)
    return rendered_pieces
