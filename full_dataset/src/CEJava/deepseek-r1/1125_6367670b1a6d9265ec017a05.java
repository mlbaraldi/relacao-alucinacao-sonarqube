package generated;
public class Generateda6659e545d12 {
public static String toString(final char ch){
    if (ch < 128) {
        return CHAR_CACHE[ch];
    }
    return new String(new char[]{ch});
}
}
