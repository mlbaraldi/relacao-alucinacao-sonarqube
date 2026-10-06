def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    import os
    """
    Write the rendered configuration YAML to the specified file, creating any necessary directories.
    If the file exists and overwrite is False, abort the operation.
    """
    if os.path.exists(config_filename) and not overwrite:
        return
    
    directory = os.path.dirname(config_filename)
    if directory:  # Only create directories if the path is not empty
        os.makedirs(directory, exist_ok=True)
    
    with open(config_filename, 'w') as f:
        f.write(rendered_config)
    
    os.chmod(config_filename, mode)
