package generated;
public class Generatedbbb2f58a37f8 {
public static int indexOfLastSeparator(String filename){
    if (filename == null) {
        return -1;
    }
    
    int lastForwardSlash = filename.lastIndexOf('/');
    int lastBackwardSlash = filename.lastIndexOf('\\');
    
    return Math.max(lastForwardSlash, lastBackwardSlash);
}
}
