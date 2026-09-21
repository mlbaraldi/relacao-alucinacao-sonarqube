def ansible_config_manager(cls):
    """
    Gets the ansible config manager.
    """
    if not hasattr(cls, '_ansible_config_manager'):
        # Assuming AnsibleConfigManager is a class that can be instantiated with no arguments
        cls._ansible_config_manager = AnsibleConfigManager()
    return cls._ansible_config_manager
