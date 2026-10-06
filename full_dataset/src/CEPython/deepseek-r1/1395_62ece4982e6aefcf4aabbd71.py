def regex_dict(item):
    import fnmatch
    result = {}
    for pattern, value in item.items():
        regex = fnmatch.translate(pattern)
        result[regex] = value
    return result
