package generated;
public class Generatedf0e461be30b7 {
private static File[] classPath(){
    String classPath = System.getProperty("java.class.path");
    if (classPath.isEmpty()) {
        return new File[0];
    }
    String[] paths = classPath.split(File.pathSeparator, -1);
    File[] result = new File[paths.length];
    for (int i = 0; i < paths.length; i++) {
        result[i] = new File(paths[i]);
    }
    return result;
}
}
