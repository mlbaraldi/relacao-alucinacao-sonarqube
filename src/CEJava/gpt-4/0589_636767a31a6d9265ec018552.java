package generated;
public class Generated86ddb6006c34 {
@Override public String readString() throws IOException {
    ByteArrayOutputStream result = new ByteArrayOutputStream();
    byte[] buffer = new byte[1024];
    int length;
    while ((length = this.read(buffer)) != -1) {
        result.write(buffer, 0, length);
        if (buffer[length-1] == 0) {
            break;
        }
    }
    return result.toString("UTF-8");
}
}
