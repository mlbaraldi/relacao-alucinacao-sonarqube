package generated;
public class Generatedfbb11b8e0fba {
public static String deleteAny(String inString,String charsToDelete){
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < inString.length(); i++) {
        char c = inString.charAt(i);
        if (!charsToDelete.contains(c)) {
            sb.append(c);
        }
    }
    return sb.toString();
}
}
