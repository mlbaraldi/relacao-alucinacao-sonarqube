package generated;
public class Generated47a7a3a69fe2 {
@SuppressWarnings("unchecked") public static void addToClassPath(Vector<URL> cpV,String dir){
    File directory = new File(dir);
    if (!directory.isDirectory()) {
        return;
    }
    File[] files = directory.listFiles();
    if (files == null) {
        return;
    }
    for (File file : files) {
        if (file.isFile() && file.getName().toLowerCase().endsWith(".jar")) {
            try {
                URL url = file.toURI().toURL();
                cpV.add(url);
            } catch (MalformedURLException e) {
                // Ignore the exception or handle it as needed
            }
        }
    }
}
}
