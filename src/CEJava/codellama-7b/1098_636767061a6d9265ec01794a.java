package generated;
public class Generateddaff745f5289 {
public static int indexOfExtension(String filename){
    if (filename == null) {
        return -1;
    }
    int lastSeparator = indexOfLastSeparator(filename);
    if (lastSeparator == -1) {
        return -1;
    }
    int lastDot = filename.lastIndexOf('.');
    if (lastDot > lastSeparator) {
        return lastDot;
    }
    return -1;
}
}
