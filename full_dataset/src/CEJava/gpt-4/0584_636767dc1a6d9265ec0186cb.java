package generated;
public class Generated6612173a2835 {
public void init(){
    // Define the path
    String distPath = "/path/to/your/directory";

    // Create a Path object
    Path path = Paths.get(distPath);

    // Check if directory exists
    if (!Files.exists(path)) {
        try {
            // Create the directory
            Files.createDirectories(path);
            System.out.println("Directory created successfully");
        } catch (Exception e) {
            // Print the exception
            System.out.println("Failed to create directory: " + e.getMessage());
        }
    } else {
        System.out.println("Directory already exists");
    }
}
}
