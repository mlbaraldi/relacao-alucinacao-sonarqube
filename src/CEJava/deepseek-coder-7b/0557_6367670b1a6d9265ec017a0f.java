package generated;
public class Generated4b9d82421d8a {
public static boolean containsAnyIgnoreCase(String str,List<String> searchStrArray){
    if (str == null || searchStrArray == null) {
        return false;
    }

    for (String searchStr : searchStrArray) {
        if (searchStr != null && str.toLowerCase().indexOf(searchStr.toLowerCase()) != -1) {
            return true;
        }
    }

    return false;
}
}
