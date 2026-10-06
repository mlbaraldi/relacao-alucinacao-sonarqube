package generated;
public class Generated86ddb6006c34 {
@Override public String readString() throws IOException {
    int length = inputStream.readInt(); // Assuming the length of the string is stored as an integer
    byte[] bytes = new byte[length];
    inputStream.readFully(bytes);
    return new String(bytes, "UTF-8");
}
}
