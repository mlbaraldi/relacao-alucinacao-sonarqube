

def _dictsum(dicts):
    """
    Combine values of the dictionaries supplied by iterable dicts.
    """
    combined_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key in combined_dict:
                combined_dict[key] += value
            else:
                combined_dict[key] = value
    return combined_dict
