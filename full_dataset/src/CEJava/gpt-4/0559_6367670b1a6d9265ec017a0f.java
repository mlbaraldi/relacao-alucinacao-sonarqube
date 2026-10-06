package generated;
public class Generated4b9d82421d8a {
public static boolean containsAnyIgnoreCase(String str,List<String> searchStrArray){
    if (str == null || searchStrArray == null) {
        return false;
    }

    String lowerCaseStr = str.toLowerCase();

    for (String searchStr : searchStrArray) {
        if (searchStr != null && lowerCaseStr.contains(searchStr.toLowerCase())) {
            return true;
        }
    }

    return false;
}
}
