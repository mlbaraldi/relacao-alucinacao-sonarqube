package generated;
public class Generated0a21f59069a6 {
public static int computeUTF8Size(final CharSequence str,final int index,final int len){
    if (str == null) {
        throw new NullPointerException("str must not be null");
    }
    if (index < 0 || index >= str.length()) {
        throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + str.length());
    }
    if (len < 0 || index + len > str.length()) {
        throw new IllegalArgumentException("len is negative or exceeds the length of str");
    }

    String substring = str.subSequence(index, index + len).toString();
    return substring.getBytes(StandardCharsets.UTF_8).length;
}
}
