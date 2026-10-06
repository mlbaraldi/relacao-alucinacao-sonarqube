def was_processed(processed, path_name, verbose):
    import os
    abs_path = os.path.abspath(path_name)
    if abs_path in processed:
        if verbose:
            print(f"Already processed {abs_path}")
        return True
    processed.add(abs_path)
    return False
