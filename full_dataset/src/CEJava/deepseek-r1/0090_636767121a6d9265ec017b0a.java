package generated;
public class Generatedc00635d05840 {
private int parseEndOfLine(String headerPart,int end){
    int start = end + 1;
    int length = headerPart.length();
    for (int i = start; i < length - 1; i++) {
        if (headerPart.charAt(i) == '\r' && headerPart.charAt(i + 1) == '\n') {
            return i;
        }
    }
    if (start <= length - 2) {
        if (headerPart.charAt(start) == '\r' && headerPart.charAt(start + 1) == '\n') {
            return start;
        }
    }
    return -1;
}
}
