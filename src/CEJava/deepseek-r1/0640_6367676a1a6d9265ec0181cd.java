package generated;
public class Generated871088b09ca6 {
public static String trimLeadingWhitespace(String str){
    if (str == null || str.isEmpty()) {
        return str;
    }
    int start;
    for (start = 0; start < str.length(); start++) {
        if (!Character.isWhitespace(str.charAt(start))) {
            break;
        }
    }
    return str.substring(start);
}
}
