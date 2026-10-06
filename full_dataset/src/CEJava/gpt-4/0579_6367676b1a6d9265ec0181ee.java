package generated;
public class Generatede41b2c9ca7f9 {
public static String trimTrailingWhitespace(String str){
    if (str == null || str.isEmpty()) {
        return str;
    }

    int i;
    for (i = str.length() - 1; i >= 0; i--) {
        if (!Character.isWhitespace(str.charAt(i))) {
            break;
        }
    }

    return str.substring(0, i + 1);
}
}
