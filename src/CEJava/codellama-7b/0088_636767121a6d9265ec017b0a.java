package generated;
public class Generatedc00635d05840 {
private int parseEndOfLine(String headerPart,int end){
    int index = headerPart.indexOf("\r\n", end);
    if (index == -1) {
        throw new IllegalArgumentException("Invalid header: missing end of line");
    }
    return index;
}
}
