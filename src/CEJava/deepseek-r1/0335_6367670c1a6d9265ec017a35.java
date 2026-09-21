package generated;
public class Generatedf68874431de2 {
private static boolean endsWith(final String str,final String suffix,final boolean ignoreCase){
    if (str == null || suffix == null) {
        return str == suffix;
    }
    if (suffix.length() > str.length()) {
        return false;
    }
    int strBeginIndex = str.length() - suffix.length();
    String strEnd = str.substring(strBeginIndex);
    return ignoreCase ? strEnd.equalsIgnoreCase(suffix) : strEnd.equals(suffix);
}
}
