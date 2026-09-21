package generated;
public class Generated79e0e5c09e09 {
public void readFrom(final InputStream in) throws IOException {
    byte[] buffer = new byte[4096];
    int bytesRead;
    while ((bytesRead = in.read(buffer)) != -1) {
        this.buffer.add(buffer, 0, bytesRead);
    }
}
}
