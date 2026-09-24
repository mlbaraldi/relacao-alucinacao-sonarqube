package generated;
public class Generated91bfb64e4006 {
final String readUtf(final int constantPoolEntryIndex,final char[] charBuffer){
    // Assuming 'items' is an array in the class that maps constant pool indices to their offsets in classFileBuffer
    int offset = items[constantPoolEntryIndex];

    // Check if the tag is CONSTANT_Utf8 (1)
    if (classFileBuffer[offset] != 1) {
        throw new IllegalArgumentException("Entry is not a CONSTANT_Utf8");
    }

    // Read the length of the UTF-8 string
    int utfLength = ((classFileBuffer[offset + 1] & 0xFF) << 8) | (classFileBuffer[offset + 2] & 0xFF);
    int bytesStart = offset + 3;

    int count = 0;
    int charIndex = 0;

    // Process ASCII characters (0x00-0x7F)
    while (count < utfLength) {
        int c = classFileBuffer[bytesStart + count] & 0xFF;
        if (c > 127) {
            break;
        }
        // Check for invalid null character in single-byte form
        if (c == 0) {
            throw new IllegalArgumentException("Null byte in UTF-8 data");
        }
        charBuffer[charIndex++] = (char) c;
        count++;
    }

    // Process multi-byte characters
    while (count < utfLength) {
        int c = classFileBuffer[bytesStart + count] & 0xFF;
        int char2, char3;

        switch (c >> 4) {
            case 0x0:
            case 0x1:
            case 0x2:
            case 0x3:
            case 0x4:
            case 0x5:
            case 0x6:
            case 0x7:
                // Single-byte character, already handled, should not occur here
                count++;
                charBuffer[charIndex++] = (char) c;
                break;

            case 0xC:
            case 0xD:
                // Two-byte character
                if (count + 1 >= utfLength) {
                    throw new IllegalArgumentException("Malformed UTF-8: truncated two-byte character");
                }
                char2 = classFileBuffer[bytesStart + count + 1] & 0xFF;
                if ((char2 & 0xC0) != 0x80) {
                    throw new IllegalArgumentException("Malformed UTF-8 around byte " + (count + 1));
                }
                // Check for encoded null (0xC0, 0x80)
                if (c == 0xC0 && char2 == 0x80) {
                    charBuffer[charIndex++] = '\0';
                } else {
                    charBuffer[charIndex++] = (char) (((c & 0x1F) << 6) | (char2 & 0x3F));
                }
                count += 2;
                break;

            case 0xE:
                // Three-byte character
                if (count + 2 >= utfLength) {
                    throw new IllegalArgumentException("Malformed UTF-8: truncated three-byte character");
                }
                char2 = classFileBuffer[bytesStart + count + 1] & 0xFF;
                char3 = classFileBuffer[bytesStart + count + 2] & 0xFF;
                if ((char2 & 0xC0) != 0x80 || (char3 & 0xC0) != 0x80) {
                    throw new IllegalArgumentException("Malformed UTF-8 around byte " + (count + 2));
                }
                charBuffer[charIndex++] = (char) (((c & 0x0F) << 12) |
                        ((char2 & 0x3F) << 6) |
                        (char3 & 0x3F));
                count += 3;
                break;

            default:
                throw new IllegalArgumentException("Malformed UTF-8 around byte " + count);
        }
    }

    return new String(charBuffer, 0, charIndex);
}
}
