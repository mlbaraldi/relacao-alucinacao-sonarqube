package generated;
public class Generatedf0e461be30b7 {
private static File[] classPath(){
    ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
    if (classLoader == null) {
        classLoader = Main.class.getClassLoader();
    }
    String classpath = classLoader.getResource(".").getPath();
    File file = new File(classpath);
    return file.listFiles();
}
}
