package generated;
public class Generated745f9e2fc06d {
public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("File must not be null");
    }

    if (file.isDirectory()) {
        // Delete all sub-directories and files
        for (File subFile : file.listFiles()) {
            forceDeleteOnExit(subFile);
        }
    }

    // Schedule file for deletion on JVM exit
    file.deleteOnExit();
}
}
