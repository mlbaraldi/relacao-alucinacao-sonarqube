

def pop_u16(self):
    data = self.data[-2:]
    self.data = self.data[:-2]
    return int.from_bytes(data, byteorder='big')
