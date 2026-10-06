package generated;
public class Generated745f9e2fc06d {
public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("File must not be null");
    }

    if (file.isDirectory()) {
        deleteDir(file);
    } else {
        if (!file.delete()) {
            throw new IOException("Cannot delete file: " + file);
        }
    }

    Runtime.getRuntime().addShutdownHook(new Thread() {
        public void run() {
            try {
                forceDeleteOnExit(file);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    });
}
}
