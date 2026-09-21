package generated;
public class Generated178c4a579295 {
private static int decodeOctets(int i,ByteBuffer bb,StringBuilder sb){
    if (bb.hasRemaining()) {
        if (bb.get(i) < 0x80) {
            sb.append((char) bb.get(i));
            return i + 1;
        } else if ((bb.get(i) & 0xE0) == 0xC0) {
            sb.append((char) ((bb.get(i) & 0x1F) << 6 | (bb.get(i + 1) & 0x3F) << 2 | (bb.get(i + 2) & 0x3C) >> 2);
            return i + 3;
        } else if ((bb.get(i) & 0xF0) == 0xE0) {
            sb.append((char) ((bb.get(i) & 0xF) << 12 | (bb.get(i + 1) & 0x3F) << 6 | (bb.get(i + 2) & 0x3F) << 2 | (bb.get(i + 3) & 0x3C) >> 2);
            return i + 4;
        } else if ((bb.get(i) & 0xF0) == 0xF0) {
            sb.append((char) ((bb.get(i) & 0x3) << 18 | (bb.get(i + 1) & 0x3F) << 12 | (bb.get(i + 2) & 0x3F) << 6 | (bb.get(i + 3) & 0x3F) << 2 | (bb.get(i + 4) & 0x3C) >> 2);
            return i + 5;
        } else {
            throw new IllegalArgumentException("Invalid UTF-8 encoding");
        }
    } else {
        return
}
