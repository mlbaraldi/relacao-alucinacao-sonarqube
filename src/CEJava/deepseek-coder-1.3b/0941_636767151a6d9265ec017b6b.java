package generated;
public class Generated33e66cf0e1a5 {
private static boolean startsWith(final String str,final String prefix,final boolean ignoreCase){
    if (str == null || prefix == null) {
        return str == prefix;
    }

    if (ignoreCase) {
        return str.toLowerCase().startsWith(prefix.toLowerCase());
    } else {
        return str.startsWith(prefix);
    }
}
}
