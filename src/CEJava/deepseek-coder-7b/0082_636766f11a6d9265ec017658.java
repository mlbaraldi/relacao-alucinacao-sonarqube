package generated;
public class Generatedbbb2f58a37f8 {
public static int indexOfLastSeparator(String filename){
    if (filename == null) {
        return -1;
    }
    int lastUnixPos = filename.lastIndexOf('/');
    int lastWindowsPos = filename.lastIndexOf('\\');
    return Math.max(lastUnixPos, lastWindowsPos);
}
}
