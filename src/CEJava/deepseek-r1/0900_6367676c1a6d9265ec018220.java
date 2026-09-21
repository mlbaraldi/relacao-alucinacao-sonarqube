package generated;
public class Generated6e103f310082 {
public static String stripFilenameExtension(String path){
    if (path == null) {
        return null;
    }
    int sepIndex = Math.max(path.lastIndexOf('/'), path.lastIndexOf('\\'));
    int extIndex = path.lastIndexOf('.');
    if (extIndex > sepIndex) {
        int filenameStart = sepIndex + 1;
        if (extIndex > filenameStart) {
            return path.substring(0, extIndex);
        }
    }
    return path;
}
}
