package generated;
public class Generateddaff745f5289 {
public static int indexOfExtension(String filename){
    if (filename == null) {
        return -1;
    }
    int lastSeparator = indexOfLastSeparator(filename);
    int lastDot = filename.lastIndexOf('.');
    if (lastDot != -1) {
        if (lastSeparator == -1 || lastDot > lastSeparator) {
            return lastDot;
        }
    }
    return -1;
}
}
