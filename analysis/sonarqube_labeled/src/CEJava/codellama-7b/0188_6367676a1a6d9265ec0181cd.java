package generated;
public class Generated871088b09ca6 {
public static String trimLeadingWhitespace(String str){
    int start = 0;
    while (start < str.length() && Character.isWhitespace(str.charAt(start))) {
        start++;
    }
    return str.substring(start);
}
}
