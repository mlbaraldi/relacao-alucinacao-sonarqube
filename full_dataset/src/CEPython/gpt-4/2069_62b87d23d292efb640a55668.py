

def get_config():
    """
    Create, populate and return the Config object.
    """
    config = Config()
    config.add_item('version', '1.0.0')
    config.add_item('debug', True)
    return config
