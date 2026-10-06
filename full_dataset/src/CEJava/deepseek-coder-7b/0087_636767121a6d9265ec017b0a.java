package generated;
public class Generatedc00635d05840 {
private int parseEndOfLine(String headerPart,int end){
    if (end < 0 || end >= headerPart.length()) {
        throw new IllegalArgumentException("End index out of bounds");
    }
    int index = headerPart.indexOf("\r\n", end);
    return index;
}
}
