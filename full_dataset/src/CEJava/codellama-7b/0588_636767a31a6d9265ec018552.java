package generated;
public class Generated86ddb6006c34 {
@Override public String readString() throws IOException {
    int length = in.readInt();
    byte[] bytes = new byte[length];
    in.readFully(bytes);
    return new String(bytes, "UTF-8");
}
}
