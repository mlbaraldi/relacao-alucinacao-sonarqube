import os


def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    if os.path.exists(config_filename) and not overwrite:
        print(f"File {config_filename} already exists. Set overwrite=True to overwrite.")
        return

    # Create directories if they don't exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)

    with open(config_filename, 'w') as config_file:
        config_file.write(rendered_config)

    os.chmod(config_filename, mode)
