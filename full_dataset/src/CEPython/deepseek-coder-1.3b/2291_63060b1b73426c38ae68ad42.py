import os


def inject_config(self):
    """
    Set the environment variable for config path, if it is undefined.
    """
    config_path = os.getenv('CONFIG_PATH')
    if not config_path:
        os.environ['CONFIG_PATH'] = '/path/to/your/config'
    else:
        print(f'CONFIG_PATH is already set to {config_path}')
