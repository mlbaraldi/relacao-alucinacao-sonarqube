package generated;
public class Generated47a7a3a69fe2 {
@SuppressWarnings("unchecked") public static void addToClassPath(Vector<URL> cpV,String dir){
    File directory = new File(dir);
    File[] files = directory.listFiles();

    if (files != null) {
        for (File file : files) {
            if (file.isFile() && file.getName().endsWith(".jar")) {
                try {
                    cpV.add(file.toURI().toURL());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
}
