import os


def find_path_type(path):
    if os.path.isdir(path):
        # Check for "0=*" file to determine directory type
        for filename in os.listdir(path):
            if filename.startswith("0="):
                if filename[2:] == "ocfl_object_1.0":
                    return 'object'
                elif filename[2:] == "ocfl_1.0":
                    return 'root'
        # If no "0=*" file found, return error message
        return 'Directory does not contain a "0=*" file'
    elif os.path.isfile(path):
        return 'file'
    else:
        return 'Path does not exist or is not a file or directory'
