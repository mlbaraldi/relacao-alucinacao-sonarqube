package generated;
public class Generateda70133497692 {
public static LinkedBuffer writeUTF8(final CharSequence str,final WriteSession session,final LinkedBuffer lb){
    int strLen = str.length();
    int charIndex = 0;
    while (charIndex < strLen) {
        char c = str.charAt(charIndex);
        if (c <= 0x7F) {
            lb.writeByte((byte) c);
        } else if (c <= 0x7FF) {
            lb.writeByte((byte) (0xC0 | (c >> 6)));
            lb.writeByte((byte) (0x80 | (c & 0x3F)));
        } else if (c <= 0xFFFF) {
            lb.writeByte((byte) (0xE0 | (c >> 12)));
            lb.writeByte((byte) (0x80 | ((c >> 6) & 0x3F)));
            lb.writeByte((byte) (0x80 | (c & 0x3F)));
        } else {
            lb.writeByte((byte) (0xF0 | (c >> 18)));
            lb.writeByte((byte) (0x80 | ((c >> 12) & 0x3F)));
            lb.writeByte((byte) (0x80 | ((c >> 6) & 0x3F)));
            lb.writeByte((byte) (0x80 | (c & 0x3F)));
        }
        charIndex++;
    }
    return lb;
}
}
