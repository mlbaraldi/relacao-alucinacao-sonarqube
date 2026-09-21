package generated;
public class Generated178c4a579295 {
private static int decodeOctets(int i,ByteBuffer bb,StringBuilder sb){
    // Check if the current byte is a continuation byte
    if ((bb.get(i) & 0x80) == 0) {
        // If it's not a continuation byte, it's a single-byte character
        sb.append((char) bb.get(i));
        return i + 1;
    }

    // If it's a continuation byte, it's part of a multi-byte character
    int byteCount = 1;
    while ((bb.get(i + byteCount) & 0x80) != 0) {
        byteCount++;
    }

    // Decode the multi-byte character
    int codePoint = 0;
    for (int j = 0; j < byteCount; j++) {
        codePoint <<= 6;
        codePoint |= (bb.get(i + j) & 0x3F);
    }

    // Append the decoded character to the string
    sb.append((char) codePoint);

    // Return the index to the next unchecked character in the string
    return i + byteCount;
}
}
