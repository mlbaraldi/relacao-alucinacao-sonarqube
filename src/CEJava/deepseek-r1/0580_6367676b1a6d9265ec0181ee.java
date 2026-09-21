package generated;
public class Generatede41b2c9ca7f9 {
public static String trimTrailingWhitespace(String str){
    if (str == null) {
        return null;
    }
    int end = str.length() - 1;
    while (end >= 0 && Character.isWhitespace(str.charAt(end))) {
        end--;
    }
    return end == -1 ? "" : str.substring(0, end + 1);
}
}
