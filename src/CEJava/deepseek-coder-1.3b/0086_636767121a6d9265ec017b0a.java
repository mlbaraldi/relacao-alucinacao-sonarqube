package generated;
public class Generatedc00635d05840 {
private int parseEndOfLine(String headerPart,int end){
    int currentIndex = end;
    while (currentIndex < headerPart.length() && headerPart.charAt(currentIndex) != '\n') {
        currentIndex++;
    }
    return currentIndex;
}
}
