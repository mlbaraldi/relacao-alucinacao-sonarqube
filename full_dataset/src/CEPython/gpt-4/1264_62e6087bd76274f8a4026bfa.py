

def pop_u16(self):
    # Check if there is enough data
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop_u16")

    # Get the last two bytes
    last_two_bytes = self.data[-2:]

    # Remove the last two bytes from the data
    self.data = self.data[:-2]

    # Convert the bytes to a big-endian 16-bit unsigned integer
    u16 = int.from_bytes(last_two_bytes, byteorder='big', signed=False)

    return u16
