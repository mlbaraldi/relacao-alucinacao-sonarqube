import fnmatch


def make_find_paths(find_paths):
    transformed_paths = []
    for path in find_paths:
        if not fnmatch.fnmatch(path, '*:*'):
            path = 'sh:**/*' + path + '*/**'
        transformed_paths.append(path)
    return transformed_paths
