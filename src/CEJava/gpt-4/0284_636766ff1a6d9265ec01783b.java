package generated;
public class Generated6a24a3441146 {
public static String sub(String str,int start,int end){
    // Check if the string is null or empty
    if (str == null || str.isEmpty()) {
        return str;
    }

    // Check if start is greater than end or start is greater than string length
    if (start > end || start > str.length()) {
        return "";
    }

    // Check if end is greater than string length
    if (end > str.length()) {
        end = str.length();
    }

    // Check if start is less than 0
    if (start < 0) {
        start = 0;
    }

    // Return the substring
    return str.substring(start, end);
}
}
