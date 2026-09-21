package generated;
public class Generated0a21f59069a6 {
public static int computeUTF8Size(final CharSequence str,final int index,final int len){
    int totalSize = 0;
    final int end = index + len;
    for (int i = index; i < end; ) {
        final char c = str.charAt(i);
        if (Character.isHighSurrogate(c)) {
            if (i + 1 < end) {
                final char next = str.charAt(i + 1);
                if (Character.isLowSurrogate(next)) {
                    // Valid surrogate pair, compute code point
                    final int codePoint = Character.toCodePoint(c, next);
                    if (codePoint < 0x80) {
                        totalSize += 1;
                    } else if (codePoint < 0x800) {
                        totalSize += 2;
                    } else if (codePoint < 0x10000) {
                        totalSize += 3;
                    } else {
                        totalSize += 4;
                    }
                    i += 2;
                    continue;
                }
            }
            // Treat as single high surrogate
            if (c < 0x80) {
                totalSize += 1;
            } else if (c < 0x800) {
                totalSize += 2;
            } else {
                totalSize += 3;
            }
            i++;
        } else {
            // Process as a single code unit
            final int codePoint = c;
            if (codePoint < 0x80) {
                totalSize += 1;
            } else if (codePoint < 0x800) {
                totalSize += 2;
            } else {
                totalSize += 3;
            }
            i++;
        }
    }
    return totalSize;
}
}
