package generated;
public class Generated9f261c98a83f {
protected static void deleteFile(String fileName){
    File file = new File(fileName);
    if (file.exists() && file.isFile()) {
        file.delete();
    }
}
}
