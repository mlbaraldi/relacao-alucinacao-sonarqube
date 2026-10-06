

def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    parts = target.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        i = int(item)
        if i < 0 or i > 255:
            return False
    return True
