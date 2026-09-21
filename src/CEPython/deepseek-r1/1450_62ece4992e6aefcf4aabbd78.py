def is_local(host):
    import ipaddress
    """
    Checks if the host is the localhost

    :param host: The hostname or ip
    :return: True if the host is the localhost
    """
    stripped_host = host.strip()
    if stripped_host.lower() == 'localhost':
        return True
    try:
        addr = ipaddress.ip_address(stripped_host)
        return addr.is_loopback
    except ValueError:
        return False
