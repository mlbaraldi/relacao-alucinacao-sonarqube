package generated;
public class Generated1f25d2d859d7 {
public long readRawVarint64() throws IOException {
    long result = 0;
    int shift = 0;
    while (true) {
        int b = inputStream.read();
        if (b == -1) {
            throw new EOFException();
        }
        result |= (long)(b & 0x7F) << shift;
        if ((b & 0x80) == 0) {
            break;
        }
        shift += 7;
    }
    return result;
}
}
