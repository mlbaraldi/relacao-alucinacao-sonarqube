package generated;
public class Generated215e740545c9 {
public InputStream next() throws IOException {
    if (index < files.length) {
        File file = files[index];
        index++;
        return new FileInputStream(file);
    } else {
        return null;
    }
}
}
