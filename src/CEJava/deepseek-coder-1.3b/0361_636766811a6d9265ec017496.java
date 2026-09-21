package generated;
public class Generated215e740545c9 {
public InputStream next() throws IOException {
    if (!hasNext()) {
        return null;
    }
    try {
        return new FileInputStream(currentFile);
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}
}
