package generated;
public class Generatedf68874431de2 {
private static boolean endsWith(final String str,final String suffix,final boolean ignoreCase){
    if (str == null || suffix == null) {
        return str == null && suffix == null;
    }

    if (ignoreCase) {
        return str.toUpperCase().endsWith(suffix.toUpperCase());
    } else {
        return str.endsWith(suffix);
    }
}
}
