

def was_processed(processed, path_name, verbose):
    # Expand the path name to an absolute path
    path_name = os.path.abspath(path_name)

    # Check if the path is already in the set
    if path_name in processed:
        if verbose:
            print(f"{path_name} has already been processed")
        return True

    # Add the path to the set and return False
    processed.add(path_name)
    return False
