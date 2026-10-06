package generated;
public class Generated2258a3c2deaa {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    if (byteArrayValue == null) {
        byte[] newBytes = new byte[bytes.length + byteLength];
        System.arraycopy(bytes, 0, newBytes, 0, bytes.length);
        bytes = newBytes;
        return this;
    }

    byte[] newBytes = new byte[bytes.length + byteLength];
    System.arraycopy(bytes, 0, newBytes, 0, bytes.length);
    System.arraycopy(byteArrayValue, byteOffset, newBytes, bytes.length, byteLength);
    bytes = newBytes;
    return this;
}
}
