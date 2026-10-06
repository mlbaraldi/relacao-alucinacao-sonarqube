package generated;
public class Generatedfbb11b8e0fba {
public static String deleteAny(String inString,String charsToDelete){
    if (inString == null) {
        return null;
    }
    if (charsToDelete == null || charsToDelete.isEmpty()) {
        return inString;
    }
    
    Set<Character> toDelete = new HashSet<>();
    for (int i = 0; i < charsToDelete.length(); i++) {
        toDelete.add(charsToDelete.charAt(i));
    }
    
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < inString.length(); i++) {
        char c = inString.charAt(i);
        if (!toDelete.contains(c)) {
            result.append(c);
        }
    }
    return result.toString();
}
}
