def list_of_file_names(settings_dirs, spec_option):
    import os
    """
    Create a new IniType complex type by generating a list of file paths.
    Each file path is formed by joining each directory in settings_dirs with the spec_option.
    """
    return [os.path.join(d, spec_option) for d in settings_dirs]
