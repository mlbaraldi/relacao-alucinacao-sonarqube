

def render(pieces, style):
    if style == "plain":
        return "".join(pieces)
    elif style == "bold":
        return "".join(["**" + piece + "**" for piece in pieces])
    elif style == "italic":
        return "".join(["*" + piece + "*" for piece in pieces])
    elif style == "strikethrough":
        return "".join(["~~" + piece + "~~" for piece in pieces])
    else:
        raise ValueError("Invalid style")
