package generated;
public class Generateda70133497692 {
public static LinkedBuffer writeUTF8(final CharSequence str,final WriteSession session,final LinkedBuffer lb){
    int length = str.length();
    int index = 0;
    LinkedBuffer currentLB = lb;
    byte[] temp = new byte[4];
    
    while (index < length) {
        int codePoint = Character.codePointAt(str, index);
        index += Character.charCount(codePoint);
        
        int numBytes;
        if (codePoint <= 0x7F) {
            numBytes = 1;
            temp[0] = (byte) codePoint;
        } else if (codePoint <= 0x7FF) {
            numBytes = 2;
            temp[0] = (byte) (0xC0 | (codePoint >> 6));
            temp[1] = (byte) (0x80 | (codePoint & 0x3F));
        } else if (codePoint <= 0xFFFF) {
            numBytes = 3;
            temp[0] = (byte) (0xE0 | (codePoint >> 12));
            temp[1] = (byte) (0x80 | ((codePoint >> 6) & 0x3F));
            temp[2] = (byte) (0x80 | (codePoint & 0x3F));
        } else {
            numBytes = 4;
            temp[0] = (byte) (0xF0 | (codePoint >> 18));
            temp[1] = (byte) (0x80 | ((codePoint >> 12) & 0x3F));
            temp[2] = (byte) (0x80 | ((codePoint >> 6) & 0x3F));
            temp[3] = (byte) (0x80 | (codePoint & 0x3F));
        }
        
        int j = 0;
        while (j < numBytes) {
            int remaining = currentLB.buffer.length - currentLB.offset;
            if (remaining == 0) {
                currentLB = session.nextBuffer(currentLB);
                remaining = currentLB.buffer.length - currentLB.offset;
            }
            int bytesToCopy = Math.min(remaining, numBytes - j);
            System.arraycopy(temp, j, currentLB.buffer, currentLB.offset, bytesToCopy);
            currentLB.offset += bytesToCopy;
            j += bytesToCopy;
        }
    }
    
    return lb;
}
}
