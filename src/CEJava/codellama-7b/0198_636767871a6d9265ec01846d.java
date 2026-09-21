package generated;
public class Generated7a1c09d1514a {
public static void createConfigurationDirectory(){
    String configDir = System.getProperty("user.home") + File.separator + "lf5";
    File configDirFile = new File(configDir);
    if (!configDirFile.exists()) {
        configDirFile.mkdirs();
    }
}
}
