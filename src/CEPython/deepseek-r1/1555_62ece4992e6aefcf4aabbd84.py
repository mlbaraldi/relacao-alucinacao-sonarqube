def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    parts = target.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        # Check if part is numeric and does not have leading zeros unless it's '0'
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True
