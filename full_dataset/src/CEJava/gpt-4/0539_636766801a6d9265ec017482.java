package generated;
public class Generated79e0e5c09e09 {
public void readFrom(final InputStream in) throws IOException {
    ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
    byte[] chunk = new byte[1024];
    int bytesRead;

    while ((bytesRead = in.read(chunk)) != -1) {
        byteArrayOutputStream.write(chunk, 0, bytesRead);
    }

    buffer = byteArrayOutputStream.toByteArray();
    readPointer = 0;
}
}
