package generated;
public class Generateda6659e545d12 {
public static String toString(final char ch){
    if (ch < 128) {
        return ASCII_CHARS[ch];
    } else {
        return new String(new char[] { ch });
    }
}
}
