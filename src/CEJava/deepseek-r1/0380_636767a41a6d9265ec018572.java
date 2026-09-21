package generated;
public class Generated1f25d2d859d7 {
public long readRawVarint64() throws IOException {
    long result = 0;
    for (int i = 0; i < 10; i++) {
        final int b = input.read();
        if (b == -1) {
            throw new EOFException("End of stream encountered while reading varint.");
        }
        if (i == 9) {
            int value = b & 0x7F;
            if (value > 0x01) {
                throw new IOException("Overflow in varint decoding.");
            }
        }
        result |= (long) (b & 0x7F) << (7 * i);
        if ((b & 0x80) == 0) {
            return result;
        }
    }
    throw new IOException("Malformed varint: too many bytes");
}
}
