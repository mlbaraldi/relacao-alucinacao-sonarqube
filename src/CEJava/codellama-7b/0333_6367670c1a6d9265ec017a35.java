package generated;
public class Generatedf68874431de2 {
private static boolean endsWith(final String str,final String suffix,final boolean ignoreCase){
    if (str == null || suffix == null) {
        return false;
    }
    if (ignoreCase) {
        return str.toLowerCase().endsWith(suffix.toLowerCase());
    } else {
        return str.endsWith(suffix);
    }
}
}
