import glob


def make_find_paths(find_paths):
    new_find_paths = []
    for path in find_paths:
        if ':' in path:
            # If the path contains a colon, it's a pattern, so pass it through untouched
            new_find_paths.append(path)
        else:
            # Otherwise, transform the path fragment into a glob pattern
            new_find_paths.append(glob.glob(path))
    return new_find_paths
