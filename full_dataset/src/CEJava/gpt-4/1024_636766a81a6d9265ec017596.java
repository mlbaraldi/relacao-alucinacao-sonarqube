package generated;
public class Generated7746ec4e0a66 {
public ByteVector putInt(final int intValue){
    byte[] intBytes = ByteBuffer.allocate(4).putInt(intValue).array();
    for (byte b : intBytes) {
        this.bytes.add(b);
    }
    return this;
}
}
