

def test_tag(tag: str) -> bool:
    # Check if the tag is a valid string
    if not isinstance(tag, str):
        return False

    # Check if the tag is not empty
    if len(tag) == 0:
        return False

    # Check if the tag contains only alphanumeric characters and underscores
    if not tag.isalnum() and not tag.endswith('_'):
        return False

    # Check if the tag is not a reserved word
    if tag in ['and', 'or', 'not', 'in', 'is', 'for', 'while', 'if', 'else', 'elif', 'except', 'finally']:
        return False

    return True
