package generated;
public class Generated1f25d2d859d7 {
public long readRawVarint64() throws IOException {
    long result = 0;
    int shift = 0;
    int b;
    do {
        b = in.read();
        result |= (b & 0x7F) << shift;
        shift += 7;
    } while ((b & 0x80) != 0);
    return result;
}
}
