import fnmatch
import os


def make_find_paths(find_paths):
    """
    Given a sequence of path fragments or patterns as passed to `--find`, transform all path
    fragments into glob patterns. Pass through existing patterns untouched.
    """
    new_find_paths = []
    for path in find_paths:
        if ':' not in path:  # Check if the path is a pattern or a fragment
            # If it's a fragment, transform it into a glob pattern
            new_path = 'sh:**/*' + fnmatch.translate(path) + '*'
            new_find_paths.append(new_path)
        else:
            # If it's a pattern, pass it through untouched
            new_find_paths.append(path)
    return new_find_paths
