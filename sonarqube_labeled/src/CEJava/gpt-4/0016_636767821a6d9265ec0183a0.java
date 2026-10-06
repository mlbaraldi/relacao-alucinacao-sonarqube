package generated;
public class Generated9f261c98a83f {
protected static void deleteFile(String fileName){
    try {
        Path filePath = Paths.get(fileName);
        if (Files.exists(filePath)) {
            Files.delete(filePath);
            System.out.println("File deleted successfully");
        } else {
            System.out.println("File does not exist");
        }
    } catch (Exception e) {
        System.out.println("An error occurred while deleting the file");
        e.printStackTrace();
    }
}
}
