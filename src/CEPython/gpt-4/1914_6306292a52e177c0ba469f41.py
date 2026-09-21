

def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    if isinstance(tag, str) and len(tag) > 0 and ' ' not in tag:
        return True
    else:
        return False
