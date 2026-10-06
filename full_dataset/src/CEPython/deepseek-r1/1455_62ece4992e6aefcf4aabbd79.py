def make_find_paths(find_paths):
    transformed = []
    for path in find_paths:
        if ':' in path:
            transformed.append(path)
        else:
            transformed.append(f'sh:**/*{path}*/**')
    return transformed
