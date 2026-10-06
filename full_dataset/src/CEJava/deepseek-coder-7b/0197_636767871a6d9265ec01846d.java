package generated;
public class Generated7a1c09d1514a {
public static void createConfigurationDirectory(){
    String userHome = System.getProperty("user.home");
    File configDir = new File(userHome, "lf5");

    if (!configDir.exists()) {
        if (configDir.mkdirs()) {
            System.out.println("Directory created successfully");
        } else {
            System.out.println("Failed to create directory");
        }
    } else {
        System.out.println("Directory already exists");
    }
}
}
