

def find_path_type(path):
    # Check if the path is a root directory
    if path == '/':
        return 'root'

    # Check if the path is an OCFL Object
    if path.endswith('/'):
        return 'object'

    # Check if the path is a file
    if path.endswith('.txt'):
        return 'file'

    # Check if the path is an inventory file
    if path.endswith('.inv'):
        return 'inventory'

    # If none of the above conditions are met, return an error message
    return 'Invalid path'
