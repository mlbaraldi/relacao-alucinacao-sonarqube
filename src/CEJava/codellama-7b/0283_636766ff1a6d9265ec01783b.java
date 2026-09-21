package generated;
public class Generated6a24a3441146 {
public static String sub(String str,int start,int end){
    if (str == null || start < 0 || end < 0 || start > end) {
        return null;
    }
    int length = str.length();
    if (start >= length || end >= length) {
        return null;
    }
    return str.substring(start, end);
}
}
