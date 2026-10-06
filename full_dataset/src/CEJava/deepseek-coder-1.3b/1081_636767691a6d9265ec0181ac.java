package generated;
public class Generated2ce65cd9c4a0 {
public static String applyRelativePath(String path,String relativePath){
    try {
        Path basePath = Paths.get(path);
        Path relative = Paths.get(relativePath);
        Path absolute = basePath.resolve(relative);
        return absolute.toString();
    } catch (InvalidPathException e) {
        System.out.println("Invalid path: " + relativePath);
        return null;
    }
}
}
