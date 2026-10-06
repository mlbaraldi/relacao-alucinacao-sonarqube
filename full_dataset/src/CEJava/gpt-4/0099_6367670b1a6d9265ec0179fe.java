package generated;
public class Generated072fc6a58d02 {
@Override public void write(byte b[]) throws IOException {
    if (b == null) {
        throw new NullPointerException("Byte array cannot be null");
    }
    try {
        outputStream.write(b);
    } catch (IOException e) {
        throw new IOException("An error occurred while writing to the output stream", e);
    }
}
}
