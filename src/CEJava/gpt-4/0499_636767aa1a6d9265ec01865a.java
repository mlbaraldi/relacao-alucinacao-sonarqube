package generated;
public class Generatedf6cceee80136 {
public static int writeTo(final DataOutput out,LinkedBuffer node) throws IOException {
    int totalContentSize = 0;

    while (node != null) {
        byte[] data = node.getData();
        out.write(data);
        totalContentSize += data.length;
        node = node.getNext();
    }

    return totalContentSize;
}
}
