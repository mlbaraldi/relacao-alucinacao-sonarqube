import os
import yaml


def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered_config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    # Check if file exists and if overwrite is False
    if os.path.exists(config_filename) and not overwrite:
        print(f"File {config_filename} already exists and overwrite is set to False. Aborting.")
        return

    # Create directories if they don't exist
    dir_name = os.path.dirname(config_filename)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Write the config to file
    with open(config_filename, 'w') as file:
        yaml.dump(rendered_config, file)

    # Set the file permissions
    os.chmod(config_filename, mode)
