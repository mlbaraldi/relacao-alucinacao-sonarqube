package generated;
public class Generated6612173a2835 {
public void init(){
    if (distPath == null || distPath.trim().isEmpty()) {
        throw new IllegalStateException("Dist path is not configured");
    }

    File distDir = new File(distPath);
    if (!distDir.exists()) {
        boolean created = distDir.mkdirs();
        if (!created) {
            throw new RuntimeException("Failed to create dist directory at " + distPath);
        }
    } else {
        if (!distDir.isDirectory()) {
            throw new RuntimeException("Dist path is not a directory: " + distPath);
        }
        if (!distDir.canWrite()) {
            throw new RuntimeException("Dist directory is not writable: " + distPath);
        }
    }
}
}
