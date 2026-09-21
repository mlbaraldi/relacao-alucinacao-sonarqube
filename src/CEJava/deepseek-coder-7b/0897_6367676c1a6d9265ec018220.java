package generated;
public class Generated6e103f310082 {
public static String stripFilenameExtension(String path){
    if (path == null) {
        return null;
    }
    int extensionPos = path.lastIndexOf(".");
    if (extensionPos == -1) {
        return path;
    }
    return path.substring(0, extensionPos);
}
}
