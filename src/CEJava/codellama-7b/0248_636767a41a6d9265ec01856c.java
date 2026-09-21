package generated;
public class Generated0a21f59069a6 {
public static int computeUTF8Size(final CharSequence str,final int index,final int len){
    int size = 0;
    for (int i = index; i < index + len; i++) {
        char c = str.charAt(i);
        if (c <= 0x7F) {
            size++;
        } else if (c <= 0x7FF) {
            size += 2;
        } else if (c <= 0xFFFF) {
            size += 3;
        } else {
            size += 4;
        }
    }
    return size;
}
}
