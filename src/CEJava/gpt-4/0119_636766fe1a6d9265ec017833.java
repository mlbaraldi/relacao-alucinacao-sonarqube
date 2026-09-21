package generated;
public class Generated745f9e2fc06d {
public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("File must not be null");
    }

    if (file.isDirectory()) {
        Files.walk(Paths.get(file.getAbsolutePath()))
                .sorted(Comparator.reverseOrder())
                .map(Path::toFile)
                .forEach(File::deleteOnExit);
    } else {
        file.deleteOnExit();
    }
}
}
