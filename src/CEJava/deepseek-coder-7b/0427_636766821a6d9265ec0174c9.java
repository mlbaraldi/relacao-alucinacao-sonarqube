package generated;
public class Generatedf0e461be30b7 {
private static File[] classPath(){
    String classpath = System.getProperty("java.class.path");
    String[] classpathElements = classpath.split(File.pathSeparator);
    File[] classpathFiles = new File[classpathElements.length];
    for (int i = 0; i < classpathElements.length; i++) {
        classpathFiles[i] = new File(classpathElements[i]);
    }
    return classpathFiles;
}
}
