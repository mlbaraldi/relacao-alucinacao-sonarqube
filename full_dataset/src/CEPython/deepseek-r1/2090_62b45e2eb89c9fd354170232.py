def next_version(version):
    parts = version.split('.')
    if not parts:
        return '1'
    
    last_part = parts[-1]
    original_length = len(last_part)
    leading_zero = len(last_part) > 1 and last_part.startswith('0')
    
    num = int(last_part)
    num += 1
    new_last = str(num)
    
    if leading_zero:
        new_last = new_last.zfill(original_length)
    
    parts[-1] = new_last
    return '.'.join(parts)
