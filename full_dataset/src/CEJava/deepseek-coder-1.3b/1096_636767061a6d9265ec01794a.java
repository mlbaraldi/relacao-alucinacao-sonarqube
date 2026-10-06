package generated;
public class Generateddaff745f5289 {
public static int indexOfExtension(String filename){
    if (filename == null) {
        return -1;
    }

    int lastDot = filename.lastIndexOf('.');
    if (lastDot == -1) {
        return -1;
    }

    int lastSeparator = filename.lastIndexOf(File.separatorChar);
    if (lastDot < lastSeparator) {
        return lastDot;
    } else {
        return -1;
    }
}
}
