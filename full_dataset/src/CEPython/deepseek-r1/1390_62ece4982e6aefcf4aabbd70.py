def os_is_mac():
    import sys
    """
    Checks if the os is macOS

    :return: True if macOS
    :rtype: bool
    """
    return sys.platform == 'darwin'
