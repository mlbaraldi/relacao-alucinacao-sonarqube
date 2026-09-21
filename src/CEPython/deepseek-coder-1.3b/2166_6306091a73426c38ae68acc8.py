import os


def list_of_file_names(settings_dirs, spec_option):
    """
    Create a new IniType complex type
    """
    result = []
    for dir in settings_dirs:
        if os.path.isdir(dir):
            for root, dirs, files in os.walk(dir):
                for file in files:
                    if file.endswith(spec_option):
                        result.append(os.path.join(root, file))
        else:
            print(f"{dir} is not a directory")
    return result
