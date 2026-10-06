package generated;
public class Generated74c1a6c36636 {
public static int lastIndexOf(String str,String searchStr){
    if (str == null || searchStr == null) {
        return -1;
    }
    if (searchStr.isEmpty()) {
        return str.length();
    }
    return str.lastIndexOf(searchStr);
}
}
