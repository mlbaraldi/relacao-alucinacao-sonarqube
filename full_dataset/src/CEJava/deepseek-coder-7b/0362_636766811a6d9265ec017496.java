package generated;
public class Generated215e740545c9 {
public InputStream next() throws IOException {
    if (currentIndex >= files.size()) {
        return null;
    }

    File file = files.get(currentIndex);
    currentIndex++;

    // Assuming that the file can be opened as an InputStream
    return new FileInputStream(file);
}
}
