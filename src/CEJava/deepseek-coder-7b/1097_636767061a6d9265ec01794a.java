package generated;
public class Generateddaff745f5289 {
public static int indexOfExtension(String filename){
    if (filename == null) {
        return -1;
    }
    int extensionPos = filename.lastIndexOf(".");
    int lastSeparator = indexOfLastSeparator(filename);
    return (lastSeparator > extensionPos ? -1 : extensionPos);
}
}
