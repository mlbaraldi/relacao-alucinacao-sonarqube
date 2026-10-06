package generated;
public class Generated82d678fbe6a9 {
public static boolean isDigits(String str){
    if (str == null || str.isEmpty()) {
        return false;
    }
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (!Character.isDigit(c)) {
            return false;
        }
    }
    return true;
}
}
