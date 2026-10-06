def pop_u16(self):
    """
    Remove the last two bytes of data, returning them as a big-endian
    16-bit unsigned integer.
    """
    low = self.data.pop()
    high = self.data.pop()
    return (high << 8) | low
