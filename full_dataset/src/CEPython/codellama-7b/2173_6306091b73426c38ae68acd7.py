import ansible.config.manager
from ansible.config.manager import ansible_config_manager


def ansible_config_manager(cls):
    return ansible.config.manager.ConfigManager()
