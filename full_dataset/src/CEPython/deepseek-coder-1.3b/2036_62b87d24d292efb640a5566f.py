

def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == 'plain':
        return ' '.join(pieces)
    elif style == 'markdown':
        return '# ' + '# '.join(pieces)
    elif style == 'html':
        return '<ul>' + ''.join(['<li>' + piece + '</li>' for piece in pieces]) + '</ul>'
    else:
        raise ValueError('Unsupported style: ' + style)
