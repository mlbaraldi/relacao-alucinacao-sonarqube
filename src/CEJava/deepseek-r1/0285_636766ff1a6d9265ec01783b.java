package generated;
public class Generated6a24a3441146 {
public static String sub(String str,int start,int end){
    if (str == null) {
        return null;
    }
    int len = str.length();
    int adjustedStart = Math.max(start, 0);
    adjustedStart = Math.min(adjustedStart, len);
    int adjustedEnd = Math.max(end, 0);
    adjustedEnd = Math.min(adjustedEnd, len);
    if (adjustedStart >= adjustedEnd) {
        return "";
    }
    return str.substring(adjustedStart, adjustedEnd);
}
}
