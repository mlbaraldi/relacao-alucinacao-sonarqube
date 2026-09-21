package generated;
public class Generated4b9d82421d8a {
public static boolean containsAnyIgnoreCase(String str,List<String> searchStrArray){
    for (String searchStr : searchStrArray) {
        if (str.equalsIgnoreCase(searchStr)) {
            return true;
        }
    }
    return false;
}
}
