package generated;
public class Generated79e0e5c09e09 {
public void readFrom(final InputStream in) throws IOException {
    int bytesRead = 0;
    while (bytesRead < buffer.length) {
        int n = in.read(buffer, bytesRead, buffer.length - bytesRead);
        if (n == -1) {
            break;
        }
        bytesRead += n;
    }

    if (bytesRead < buffer.length) {
        throw new IOException("End of stream reached before all bytes were read");
    }
}
}
