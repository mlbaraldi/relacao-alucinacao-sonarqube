import re


def regex_dict(item):
    new_dict = {}
    for key, value in item.items():
        new_key = re.compile(re.escape(key).replace('\\*', '.*'))
        new_dict[new_key] = value
    return new_dict
