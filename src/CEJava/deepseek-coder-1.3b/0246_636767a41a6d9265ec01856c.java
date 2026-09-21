package generated;
public class Generated0a21f59069a6 {
public static int computeUTF8Size(final CharSequence str,final int index,final int len){
    if (str == null) {
        throw new IllegalArgumentException("Input string cannot be null");
    }

    if (index < 0 || index > str.length()) {
        throw new IllegalArgumentException("Invalid index: " + index);
    }

    if (len < 0) {
        throw new IllegalArgumentException("Invalid length: " + len);
    }

    int count = 0;
    int remaining = len;
    int currentIndex = index;

    while (remaining > 0) {
        int c = str.charAt(currentIndex);

        if ((c & 0x80) == 0) { // 0xxxxxxx
            count++;
            remaining--;
        } else if ((c & 0xe0) == 0xc0) { // 110xxxxx
            count++;
            remaining--;
        } else if ((c & 0xf0) == 0xe0) { // 1110xxxx
            count++;
            remaining--;
        } else if ((c & 0xf8) == 0xf0) { // 11110xxx
            count++;
            remaining--;
        } else {
            throw new IllegalArgumentException("Invalid character at index " + currentIndex);
        }

        currentIndex++;
    }

    return count;
}
}
