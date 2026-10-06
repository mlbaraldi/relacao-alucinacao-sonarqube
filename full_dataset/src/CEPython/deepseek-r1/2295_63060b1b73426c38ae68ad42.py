def inject_config(self):
    import os
    """
    Set the environment variable for config path, if it is undefined.
    """
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = self.config_path
