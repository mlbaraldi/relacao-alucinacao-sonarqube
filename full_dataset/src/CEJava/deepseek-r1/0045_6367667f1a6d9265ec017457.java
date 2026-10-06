package generated;
public class Generated178c4a579295 {
private static int decodeOctets(int i,ByteBuffer bb,StringBuilder sb){
    int firstOctet = bb.get(i) & 0xFF;
    int numBytes;

    if ((firstOctet & 0x80) == 0) {
        numBytes = 1;
    } else if ((firstOctet & 0xE0) == 0xC0) {
        numBytes = 2;
    } else if ((firstOctet & 0xF0) == 0xE0) {
        numBytes = 3;
    } else if ((firstOctet & 0xF8) == 0xF0) {
        numBytes = 4;
    } else {
        sb.append('\uFFFD');
        return i + 1;
    }

    if (i + numBytes > bb.limit()) {
        sb.append('\uFFFD');
        return i + 1;
    }

    for (int j = 1; j < numBytes; j++) {
        int b = bb.get(i + j) & 0xFF;
        if ((b & 0xC0) != 0x80) {
            sb.append('\uFFFD');
            return i + 1;
        }
    }

    int codePoint = 0;
    boolean invalid = false;

    switch (numBytes) {
        case 1:
            codePoint = firstOctet;
            break;
        case 2:
            int b1 = bb.get(i + 1) & 0xFF;
            codePoint = ((firstOctet & 0x1F) << 6) | (b1 & 0x3F);
            if (codePoint < 0x80) {
                invalid = true;
            }
            break;
        case 3:
            int b1_3 = bb.get(i + 1) & 0xFF;
            int b2_3 = bb.get(i + 2) & 0xFF;
            codePoint = ((firstOctet & 0x0F) << 12) | ((b1_3 & 0x3F) << 6) | (b2_3 & 0x3F);
            if (codePoint < 0x800 || (codePoint >= 0xD800 && codePoint <= 0xDFFF)) {
                invalid = true;
            }
            break;
        case 4:
            int b1_4 = bb.get(i + 1) & 0xFF;
            int b2_4 = bb.get(i + 2) & 0xFF;
            int b3_4 = bb.get(i + 3) & 0xFF;
            codePoint = ((firstOctet & 0x07) << 18) | ((b1_4 & 0x3F) << 12) | ((b2_4 & 0x3F) << 6) | (b3_4 & 0x3F);
            if (codePoint < 0x10000 || codePoint > 0x10FFFF) {
                invalid = true;
            }
            break;
        default:
            invalid = true;
            break;
    }

    if (invalid) {
        sb.append('\uFFFD');
        return i + 1;
    }

    sb.appendCodePoint(codePoint);
    return i + numBytes;
}
}
