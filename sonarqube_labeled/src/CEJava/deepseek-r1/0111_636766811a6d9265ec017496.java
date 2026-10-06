package generated;
public class Generated215e740545c9 {
public InputStream next() throws IOException {
    if (currentIndex >= files.length) {
        return null;
    }
    File nextFile = files[currentIndex++];
    return new FileInputStream(nextFile);
}
}
