import re


def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    # The regular expression pattern for a valid Python identifier
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    # Check if the tag matches the pattern
    if re.match(pattern, tag):
        return True
    else:
        return False
