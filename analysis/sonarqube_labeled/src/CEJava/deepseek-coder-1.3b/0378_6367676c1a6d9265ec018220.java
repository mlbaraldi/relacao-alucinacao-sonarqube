package generated;
public class Generated6e103f310082 {
public static String stripFilenameExtension(String path){
    if (path == null) {
        return null;
    }

    int lastDot = path.lastIndexOf('.');
    if (lastDot == -1) {
        return path;
    }

    return path.substring(0, lastDot);
}
}
