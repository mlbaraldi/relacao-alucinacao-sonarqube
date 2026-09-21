package generated;
public class Generated7a1c09d1514a {
public static void createConfigurationDirectory(){
    String userHome = System.getProperty("user.home");
    String os = System.getProperty("os.name").toLowerCase();
    String dirPath;

    if (os.contains("win") && os.contains("2000")) {
        dirPath = "C:\\Documents and Settings\\lf5";
    } else {
        dirPath = userHome + File.separator + "lf5";
    }

    File dir = new File(dirPath);
    if (!dir.exists()) {
        boolean result = dir.mkdir();
        if (!result) {
            System.out.println("Failed to create directory: " + dirPath);
        }
    }
}
}
