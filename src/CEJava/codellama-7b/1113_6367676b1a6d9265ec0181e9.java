package generated;
public class Generated63bc335b5e92 {
public static boolean substringMatch(CharSequence str,int index,CharSequence substring){
    if (str == null || substring == null) {
        return false;
    }

    int substringLength = substring.length();
    int strLength = str.length();

    if (index < 0 || index + substringLength > strLength) {
        return false;
    }

    for (int i = 0; i < substringLength; i++) {
        if (str.charAt(index + i) != substring.charAt(i)) {
            return false;
        }
    }

    return true;
}
}
