package generated;
public class Generated0a21f59069a6 {
public static int computeUTF8Size(final CharSequence str,final int index,final int len){
    int utf8Size = 0;
    for (int i = index; i < index + len; i++) {
        char ch = str.charAt(i);
        if (ch <= 0x7F) {
            utf8Size += 1;
        } else if (ch <= 0x7FF) {
            utf8Size += 2;
        } else if (Character.isHighSurrogate(ch)) {
            utf8Size += 4;
            i++;
        } else {
            utf8Size += 3;
        }
    }
    return utf8Size;
}
}
