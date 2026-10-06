def find_path_type(path):
    import os
    """
    Return a string indicating the type of thing at the given path.

    Return values:
        'root' - looks like an OCFL Storage Root
        'object' - looks like an OCFL Object
        'file' - a file, might be an inventory
        other string explains error description

    Looks only at "0=*" Namaste files to determine the directory type.
    """
    if not os.path.exists(path):
        return "Path does not exist"
    
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        root_namaste = os.path.join(path, "0=ocfl_1.0")
        if os.path.isfile(root_namaste):
            return 'root'
        object_namaste = os.path.join(path, "0=ocfl_object_1.0")
        if os.path.isfile(object_namaste):
            return 'object'
        return "Directory does not contain a root or object Namaste file"
    else:
        return "Path is not a file or directory"
