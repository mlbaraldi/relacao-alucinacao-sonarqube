import os
import shutil


def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    config_dir = os.path.dirname(config_filename)
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if os.path.exists(config_filename) and not overwrite:
        print(f"The file {config_filename} already exists and overwrite is False.")
        return

    with open(config_filename, 'w') as f:
        f.write(rendered_config)

    os.chmod(config_filename, mode)
