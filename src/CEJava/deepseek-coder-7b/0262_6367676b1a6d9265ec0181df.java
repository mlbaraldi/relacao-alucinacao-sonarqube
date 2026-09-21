package generated;
public class Generated863b88a70470 {
public static boolean startsWithIgnoreCase(String str,String prefix){
    if (str == null || prefix == null) {
        return false;
    }
    if (prefix.length() > str.length()) {
        return false;
    }
    return str.regionMatches(true, 0, prefix, 0, prefix.length());
}
}
