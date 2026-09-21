package generated;
public class Generatedf0e461be30b7 {
private static File[] classPath(){
    List<File> files = new ArrayList<>();
    ClassLoader classLoader = ClassLoader.getSystemClassLoader();
    URL[] urls = ((URLClassLoader)classLoader).getURLs();

    for(URL url: urls){
        files.add(new File(url.getFile()));
    }

    return files.toArray(new File[0]);
}
}
