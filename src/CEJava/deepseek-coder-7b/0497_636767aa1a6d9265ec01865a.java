package generated;
public class Generatedf6cceee80136 {
public static int writeTo(final DataOutput out,LinkedBuffer node) throws IOException {
    byte[] data = node.getData();
    out.write(data);
    return node.getSize();
}
}
