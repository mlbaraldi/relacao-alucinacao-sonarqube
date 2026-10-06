package generated;
public class Generated2ce65cd9c4a0 {
public static String applyRelativePath(String path,String relativePath){
    // Split the path and relative path into individual components
    String[] pathComponents = path.split("/");
    String[] relativePathComponents = relativePath.split("/");

    // Create a new array to hold the combined components
    String[] combinedComponents = new String[pathComponents.length + relativePathComponents.length];

    // Copy the path components into the combined array
    System.arraycopy(pathComponents, 0, combinedComponents, 0, pathComponents.length);

    // Copy the relative path components into the combined array
    System.arraycopy(relativePathComponents, 0, combinedComponents, pathComponents.length, relativePathComponents.length);

    // Join the combined components into a single string
    String combinedPath = String.join("/", combinedComponents);

    return combinedPath;
}
}
