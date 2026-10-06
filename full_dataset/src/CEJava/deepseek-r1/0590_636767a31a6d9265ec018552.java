package generated;
public class Generated86ddb6006c34 {
@Override public String readString() throws IOException {
    int length = readInt();
    if (length < 0) {
        throw new IOException("String length cannot be negative: " + length);
    }
    byte[] bytes = new byte[length];
    readFully(bytes);
    return new String(bytes, java.nio.charset.StandardCharsets.UTF_8);
}
}
