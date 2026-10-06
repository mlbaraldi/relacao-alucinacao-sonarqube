

def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    config = VersioneerConfig()
    config.set('key1', 'value1')
    config.set('key2', 'value2')
    return config
