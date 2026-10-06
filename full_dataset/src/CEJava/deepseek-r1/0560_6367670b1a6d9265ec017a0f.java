package generated;
public class Generated4b9d82421d8a {
public static boolean containsAnyIgnoreCase(String str,List<String> searchStrArray){
    if (str == null || searchStrArray == null || searchStrArray.isEmpty()) {
        return false;
    }
    String lowerStr = str.toLowerCase();
    for (String searchStr : searchStrArray) {
        if (searchStr == null || searchStr.isEmpty()) {
            continue;
        }
        if (lowerStr.contains(searchStr.toLowerCase())) {
            return true;
        }
    }
    return false;
}
}
