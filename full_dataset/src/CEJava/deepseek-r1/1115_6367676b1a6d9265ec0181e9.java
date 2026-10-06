package generated;
public class Generated63bc335b5e92 {
public static boolean substringMatch(CharSequence str,int index,CharSequence substring){
    if (index < 0) {
        return false;
    }
    int subLen = substring.length();
    if (index + subLen > str.length()) {
        return false;
    }
    for (int i = 0; i < subLen; i++) {
        if (str.charAt(index + i) != substring.charAt(i)) {
            return false;
        }
    }
    return true;
}
}
