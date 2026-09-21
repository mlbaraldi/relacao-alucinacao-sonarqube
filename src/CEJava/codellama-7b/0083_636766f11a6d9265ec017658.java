package generated;
public class Generatedbbb2f58a37f8 {
public static int indexOfLastSeparator(String filename){
    if (filename == null) {
        return -1;
    }
    int lastSeparator = filename.lastIndexOf('/');
    if (lastSeparator == -1) {
        lastSeparator = filename.lastIndexOf('\\');
    }
    return lastSeparator;
}
}
