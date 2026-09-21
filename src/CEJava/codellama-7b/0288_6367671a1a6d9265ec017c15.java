package generated;
public class Generated630c6f526a77 {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    if (byteArrayValue == null) {
        for (int i = 0; i < byteLength; i++) {
            this.add((byte) 0);
        }
    } else {
        for (int i = byteOffset; i < byteOffset + byteLength; i++) {
            this.add(byteArrayValue[i]);
        }
    }
    return this;
}
}
