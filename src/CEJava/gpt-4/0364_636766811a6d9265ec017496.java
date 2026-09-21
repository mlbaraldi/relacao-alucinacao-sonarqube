package generated;
public class Generated215e740545c9 {
public InputStream next() throws IOException {
    if (files.isEmpty()) {
        return null;
    } else {
        File nextFile = files.poll();
        return new FileInputStream(nextFile);
    }
}
}
