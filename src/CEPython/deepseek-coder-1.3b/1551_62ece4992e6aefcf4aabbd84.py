

def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    parts = target.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        i = int(part)
        if i < 0 or i > 255:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
    return True
