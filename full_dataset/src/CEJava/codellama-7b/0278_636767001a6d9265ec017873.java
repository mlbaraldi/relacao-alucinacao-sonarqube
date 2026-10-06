package generated;
public class Generatedc75f5c82ecf0 {
public static String reverse(final String str){
    if (str == null) {
        return null;
    }
    char[] chars = str.toCharArray();
    int length = chars.length;
    char[] reversedChars = new char[length];
    for (int i = 0; i < length; i++) {
        reversedChars[i] = chars[length - i - 1];
    }
    return new String(reversedChars);
}
}
