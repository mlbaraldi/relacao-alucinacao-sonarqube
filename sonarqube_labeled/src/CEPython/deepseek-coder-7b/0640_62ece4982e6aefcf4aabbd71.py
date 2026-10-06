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
    regex_item = {}
    for key in item.keys():
        regex_key = re.escape(key).replace('\*', '.*')
        regex_item[regex_key] = item[key]
    return regex_item
