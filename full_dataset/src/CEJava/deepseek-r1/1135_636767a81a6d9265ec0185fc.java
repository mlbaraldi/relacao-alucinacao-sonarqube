package generated;
public class Generateda9beedb4f87d {
public int readTag() throws IOException {
    int firstByte = input.read();
    if (firstByte == -1) {
        return 0;
    }

    int result = 0;
    int shift = 0;
    while (true) {
        if ((firstByte & 0x80) == 0) {
            result |= (firstByte & 0x7F) << shift;
            break;
        } else {
            result |= (firstByte & 0x7F) << shift;
            shift += 7;
            if (shift >= 32) {
                throw new IOException("Malformed varint");
            }
            int nextByte = input.read();
            if (nextByte == -1) {
                throw new EOFException("Unexpected EOF while reading varint");
            }
            firstByte = nextByte;
        }
    }

    if (result == 0) {
        throw new IOException("Encountered a tag value of zero");
    }

    return result;
}
}
