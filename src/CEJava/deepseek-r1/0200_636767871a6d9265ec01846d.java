package generated;
public class Generated7a1c09d1514a {
public static void createConfigurationDirectory(){
    String osName = System.getProperty("os.name");
    File userHome = new File(System.getProperty("user.home"));
    File configDir;

    if (osName.startsWith("Windows 2000")) {
        File parentDir = userHome.getParentFile();
        if (parentDir != null) {
            configDir = new File(parentDir, "lf5");
        } else {
            // Fallback to user.home if parent directory is not available
            configDir = new File(userHome, "lf5");
        }
    } else {
        configDir = new File(userHome, "lf5");
    }

    // Check if the directory exists; if not, attempt to create it
    if (!configDir.exists()) {
        configDir.mkdirs();
    }
}
}
