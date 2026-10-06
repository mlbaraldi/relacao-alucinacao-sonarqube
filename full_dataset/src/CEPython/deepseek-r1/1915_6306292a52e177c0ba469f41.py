def test_tag(tag: str) -> bool:
    import re
    """
    Test a word whether it could be accepted as a tag.
    A valid tag starts with a letter and contains only letters, digits, hyphens, or underscores.
    """
    return re.fullmatch(r'^[A-Za-z][A-Za-z0-9_-]*$', tag) is not None
