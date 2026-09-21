package generated;
public class Generated1f25d2d859d7 {
public long readRawVarint64() throws IOException {
    long result = 0;
    int shift = 0;

    while (true) {
        int b = in.read();
        if (b < 0) {
            throw new EOFException("Unexpected EOF");
        }

        result |= (long) (b & 0x7F) << shift;

        if ((b & 0x80) == 0) {
            return result;
        }

        shift += 7;
    }
}
}
