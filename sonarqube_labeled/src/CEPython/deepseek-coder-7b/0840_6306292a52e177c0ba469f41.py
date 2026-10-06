

def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    return tag.startswith("<") and tag.endswith(">")
