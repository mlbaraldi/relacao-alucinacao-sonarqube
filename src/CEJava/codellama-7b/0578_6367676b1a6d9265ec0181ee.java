package generated;
public class Generatede41b2c9ca7f9 {
public static String trimTrailingWhitespace(String str){
    int length = str.length();
    for (int i = length - 1; i >= 0; i--) {
        if (!Character.isWhitespace(str.charAt(i))) {
            return str.substring(0, i + 1);
        }
    }
    return "";
}
}
