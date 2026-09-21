package generated;
public class Generatedf6cceee80136 {
public static int writeTo(final DataOutput out,LinkedBuffer node) throws IOException {
    int totalSize = 0;
    while (node != null) {
        byte[] buffer = node.buffer;
        int offset = node.offset;
        int length = node.length;
        out.write(buffer, offset, length);
        totalSize += length;
        node = node.next;
    }
    return totalSize;
}
}
