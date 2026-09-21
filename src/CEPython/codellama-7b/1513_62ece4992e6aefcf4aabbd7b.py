import os
import yaml


def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    # Create any containing directories as needed
    dirname = os.path.dirname(config_filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Check if the file already exists and abort if overwrite is False
    if os.path.exists(config_filename) and not overwrite:
        raise ValueError("File already exists and overwrite is False")

    # Write the rendered config YAML to the file
    with open(config_filename, "w") as f:
        yaml.dump(rendered_config, f, default_flow_style=False)

    # Set the file mode to 0o600 if specified
    if mode is not None:
        os.chmod(config_filename, mode)
