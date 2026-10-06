package generated;
public class Generatedfbb11b8e0fba {
public static String deleteAny(String inString,String charsToDelete){
    Set<Character> deleteSet = new HashSet<>();
    for (char c : charsToDelete.toCharArray()) {
        deleteSet.add(c);
    }

    StringBuilder result = new StringBuilder();
    for (char c : inString.toCharArray()) {
        if (!deleteSet.contains(c)) {
            result.append(c);
        }
    }
    return result.toString();
}
}
