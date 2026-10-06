package generated;
public class Generatedfbb11b8e0fba {
public static String deleteAny(String inString,String charsToDelete){
    if (inString == null || charsToDelete == null) {
        return inString;
    }
    
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < inString.length(); i++) {
        char c = inString.charAt(i);
        if (charsToDelete.indexOf(c) == -1) { // if the character is not in the charsToDelete string
            sb.append(c);
        }
    }
    return sb.toString();
}
}
