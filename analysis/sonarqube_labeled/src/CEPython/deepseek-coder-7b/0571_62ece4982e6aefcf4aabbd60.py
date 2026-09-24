

def size_to_bytes(size: str) -> int:
    units = {'K': 10**3, 'M': 10**6, 'G': 10**9, 'T': 10**12}
    size_num, size_unit = ''.join(filter(str.isdigit, size)), ''.join(filter(str.isalpha, size))
    size_num = int(size_num)
    if size_unit in units:
        size_num *= units[size_unit]
    return size_num
