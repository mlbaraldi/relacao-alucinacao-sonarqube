package generated;
public class Generatedaca1cb8da825 {
private static boolean isAllZeros(String s){
    if (s == null) {
        return true;
    }
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) != '0') {
            return false;
        }
    }
    return true;
}
}
