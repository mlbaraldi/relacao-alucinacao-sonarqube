import os


def inject_config(self):
    """
    Set the environment variable for config path, if it is undefined.
    """
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = '/default/path/to/config'
