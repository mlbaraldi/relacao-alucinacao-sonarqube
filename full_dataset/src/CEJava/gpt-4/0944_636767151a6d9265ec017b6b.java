package generated;
public class Generated33e66cf0e1a5 {
private static boolean startsWith(final String str,final String prefix,final boolean ignoreCase){
    if (str == null || prefix == null) {
        return str == null && prefix == null;
    }
    if (prefix.length() > str.length()) {
        return false;
    }
    return str.regionMatches(ignoreCase, 0, prefix, 0, prefix.length());
}
}
