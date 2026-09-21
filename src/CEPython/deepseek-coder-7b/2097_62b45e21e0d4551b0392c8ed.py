

def find_path_type(path):
    """
    Return a string indicating the type of thing at the given path.

    Return values:
        'root' - looks like an OCFL Storage Root
        'object' - looks like an OCFL Object
        'file' - a file, might be an inventory
        other string explains error description

    Looks only at "0=*" Namaste files to determine the directory type.
    """
    import os

    # Check if the path exists
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    # Check if it's a directory
    if os.path.isdir(path):
        # Check for Namaste file
        namaste_file = os.path.join(path, '.namaste')
        if os.path.isfile(namaste_file):
            with open(namaste_file, 'r') as file:
                first_line = file.readline().strip()
            if first_line == "0=*":
                return 'root'
            else:
                return 'object'
        else:
            # If no Namaste file, assume it's an object
            return 'object'
    else:
        # If it's not a directory, it's a file
        return 'file'

# Example usage:
