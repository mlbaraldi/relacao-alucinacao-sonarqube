package generated;
public class Generated178c4a579295 {
private static int decodeOctets(int i,ByteBuffer bb,StringBuilder sb){
    int length = bb.remaining();
    byte[] bytes = new byte[length];
    bb.get(bytes);

    int charCount = 0;
    for (int j = 0; j < length; j++) {
        int codePoint = bytes[j] & 0xFF;

        if (codePoint >> 7 == 0) {
            // 0xxxxxxx
            sb.append((char) codePoint);
            charCount++;
        } else if (codePoint >> 5 == 0b110) {
            // 110xxxxx 10xxxxxx
            if (j + 1 >= length || (bytes[j + 1] & 0xC0) != 0x80) {
                throw new IllegalArgumentException("Invalid UTF-8 sequence");
            }
            sb.append((char) (((codePoint & 0x1F) << 6) | (bytes[++j] & 0x3F)));
            charCount += 2;
        } else if (codePoint >> 4 == 0b1110) {
            // 1110xxxx 10xxxxxx 10xxxxxx
            if (j + 2 >= length || (bytes[j + 1] & 0xC0) != 0x80 || (bytes[j + 2] & 0xC0) != 0x80) {
                throw new IllegalArgumentException("Invalid UTF-8 sequence");
            }
            sb.append((char) (((codePoint & 0x0F) << 12) | ((bytes[++j] & 0x3F) << 6) | ((bytes[++j] & 0x3F))));
            charCount += 3;
        } else if (codePoint >> 3 == 0b11110) {
            // 1
}
