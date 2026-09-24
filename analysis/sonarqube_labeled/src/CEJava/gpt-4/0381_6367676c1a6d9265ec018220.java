package generated;
public class Generated6e103f310082 {
public static String stripFilenameExtension(String path){
    if (path == null) {
        return null;
    }
    
    int dotIndex = path.lastIndexOf(".");
    if (dotIndex == -1) {
        return path;
    }
    
    return path.substring(0, dotIndex);
}
}
