import os


def was_processed(processed, path_name, verbose):
    # Expand the path name to an absolute path
    absolute_path = os.path.abspath(path_name)

    # Check if the path is already in the set
    if absolute_path in processed:
        # If verbose output is requested, report the issue
        if verbose:
            print(f"The path '{absolute_path}' has already been processed.")
        return True
    else:
        # Add the path to the set
        processed.add(absolute_path)
        return False
