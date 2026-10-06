import re


def regex_dict(item):
    """
    Convert *.cpp keys to regex keys

    Given a dict where the keys are all filenames with wildcards, convert only
    the keys into equivalent regexes and leave the values intact.

    Example:

    rules = {
        '*.cpp':
            {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h':
            {'h': 'help'}
    }
    regex_keys = regex_dict(rules)

    Args:
        item: dict to convert
    Returns:
        dict with keys converted to regexes
    """
    regex_dict = {}
    for key, value in item.items():
        if '*' in key:
            regex_key = re.sub(r'\*', '.*', key)
            regex_dict[regex_key] = value
        else:
            regex_dict[key] = value
    return regex_dict
