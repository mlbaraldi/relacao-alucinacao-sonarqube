package generated;
public class Generated33e66cf0e1a5 {
private static boolean startsWith(final String str,final String prefix,final boolean ignoreCase){
    if (str == null || prefix == null) {
        return str == null && prefix == null;
    }
    if (prefix.length() > str.length()) {
        return false;
    }
    if (ignoreCase) {
        return str.regionMatches(true, 0, prefix, 0, prefix.length());
    } else {
        return str.startsWith(prefix);
    }
}
}
