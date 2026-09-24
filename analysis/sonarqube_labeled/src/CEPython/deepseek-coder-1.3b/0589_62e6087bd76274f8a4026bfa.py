

def pop_u16(self):
    """
    Remove the last two bytes of data, returning them as a big-endian
    16-bit unsigned integer.
    """
    data = self.data[-2:]
    return int.from_bytes(data, byteorder='big', signed=False)
