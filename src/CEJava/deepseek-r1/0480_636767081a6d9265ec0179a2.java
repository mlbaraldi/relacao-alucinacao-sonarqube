package generated;
public class Generatedaca1cb8da825 {
private static boolean isAllZeros(String s){
    if (s == null) {
        return true;
    }
    int length = s.length();
    if (length == 0) {
        return false;
    }
    for (int i = 0; i < length; i++) {
        if (s.charAt(i) != '0') {
            return false;
        }
    }
    return true;
}
}
