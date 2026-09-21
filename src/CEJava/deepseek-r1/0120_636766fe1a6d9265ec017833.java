package generated;
public class Generated745f9e2fc06d {
public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("File must not be null");
    }

    if (file.isDirectory()) {
        file.deleteOnExit();

        File[] children = file.listFiles();
        if (children == null) {
            throw new IOException("Failed to list contents of directory: " + file);
        }

        for (File child : children) {
            forceDeleteOnExit(child);
        }
    } else {
        file.deleteOnExit();
    }
}
}
