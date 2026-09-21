package generated;
public class Generated9f261c98a83f {
protected static void deleteFile(String fileName){
    File file = new File(fileName);
    if (file.exists()) {
        if (file.delete()) {
            System.out.println("File deleted successfully.");
        } else {
            System.out.println("Failed to delete file.");
        }
    } else {
        System.out.println("File does not exist.");
    }
}
}
