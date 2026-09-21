package generated;
public class Generated2ce65cd9c4a0 {
public static String applyRelativePath(String path,String relativePath){
    Path basePath = Paths.get(path);
    Path relative = Paths.get(relativePath);
    Path result = basePath.getParent().resolve(relative);
    return result.toString();
}
}
