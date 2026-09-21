package generated;
public class Generated47a7a3a69fe2 {
@SuppressWarnings("unchecked") public static void addToClassPath(Vector<URL> cpV,String dir){
    File folder = new File(dir);
    File[] listOfFiles = folder.listFiles();

    if (listOfFiles != null) {
        for (File file : listOfFiles) {
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
