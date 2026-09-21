import socket


def is_local(host):
    """
    Checks if the host is the localhost

    :param host: The hostname or ip
    :return: True if the host is the localhost
    """
    localhost = socket.gethostname()
    local_ip = socket.gethostbyname(localhost)

    return host in ['localhost', '127.0.0.1', localhost, local_ip]
