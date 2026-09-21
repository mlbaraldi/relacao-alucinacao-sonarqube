package generated;
public class Generatedf6cceee80136 {
public static int writeTo(final DataOutput out,LinkedBuffer node) throws IOException {
    int totalSize = 0;
    while (node != null) {
        out.writeInt(node.getData());
        totalSize += 4;
        node = node.getNext();
    }
    return totalSize;
}
}
