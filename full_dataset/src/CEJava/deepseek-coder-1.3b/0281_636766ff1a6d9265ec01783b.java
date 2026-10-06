package generated;
public class Generated6a24a3441146 {
public static String sub(String str,int start,int end){
    if (str == null) {
        throw new IllegalArgumentException("Input string cannot be null");
    }
    if (start < 0 || end > str.length()) {
        throw new IllegalArgumentException("Invalid start or end index");
    }
    if (start > end) {
        throw new IllegalArgumentException("Start index cannot be greater than end index");
    }
    return str.substring(start, end);
}
}
