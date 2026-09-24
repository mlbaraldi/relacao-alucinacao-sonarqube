import configparser


def ansible_config_manager(cls):
    """
    Gets the ansible config manager.
    """
    config = configparser.ConfigParser()
    config.read('/etc/ansible/ansible.cfg')  # path to your ansible config file
    return config
