package generated;
public class Generated871088b09ca6 {
public static String trimLeadingWhitespace(String str){
    if (str == null || str.isEmpty()) {
        return str;
    }
    int i = 0;
    while (i < str.length() && Character.isWhitespace(str.charAt(i))) {
        i++;
    }
    return str.substring(i);
}
}
