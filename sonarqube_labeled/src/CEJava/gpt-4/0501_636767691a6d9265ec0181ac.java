package generated;
public class Generated2ce65cd9c4a0 {
public static String applyRelativePath(String path,String relativePath){
    return Paths.get(path, relativePath).normalize().toString();
}
}
