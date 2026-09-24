package generated;
public class Generated745f9e2fc06d {
public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("File must not be null");
    }

    if (file.isDirectory()) {
        for (File subFile : file.listFiles()) {
            forceDeleteOnExit(subFile);
        }
    }

    if (!file.delete()) {
        throw new IOException("Failed to delete file: " + file.getAbsolutePath());
    }
}
}
