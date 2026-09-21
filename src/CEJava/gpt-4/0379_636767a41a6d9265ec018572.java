package generated;
public class Generated1f25d2d859d7 {
public long readRawVarint64() throws IOException {
    int shift = 0;
    long result = 0;
    while (shift < 64) {
        final byte b = readByte();
        result |= (long) (b & 0x7F) << shift;
        if ((b & 0x80) == 0) {
            return result;
        }
        shift += 7;
    }
    throw new IOException("Malformed varint");
}
}
