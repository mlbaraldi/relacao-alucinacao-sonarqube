package generated;
public class Generated63bc335b5e92 {
public static boolean substringMatch(CharSequence str,int index,CharSequence substring){
    if (str == null || substring == null) {
        throw new IllegalArgumentException("Input cannot be null");
    }

    if (index + substring.length() > str.length()) {
        return false;
    }

    for (int i = 0; i < substring.length(); i++) {
        if (str.charAt(index + i) != substring.charAt(i)) {
            return false;
        }
    }

    return true;
}
}
