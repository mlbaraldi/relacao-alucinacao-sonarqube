package generated;
public class Generatedc75f5c82ecf0 {
public static String reverse(final String str){
    if (str == null) {
        return null;
    }
    char[] chars = str.toCharArray();
    int i = 0;
    int j = chars.length - 1;
    while (i < j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        i++;
        j--;
    }
    return new String(chars);
}
}
