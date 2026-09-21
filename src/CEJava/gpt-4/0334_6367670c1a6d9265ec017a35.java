package generated;
public class Generatedf68874431de2 {
private static boolean endsWith(final String str,final String suffix,final boolean ignoreCase){
    if (str == null || suffix == null) {
        return str == null && suffix == null;
    }
    if (suffix.length() > str.length()) {
        return false;
    }
    int strOffset = str.length() - suffix.length();
    return str.regionMatches(ignoreCase, strOffset, suffix, 0, suffix.length());
}
}
