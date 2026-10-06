package generated;
public class Generated2258a3c2deaa {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    if (byteLength < 0) {
        throw new IllegalArgumentException("byteLength < 0");
    }

    int newSize = size + byteLength;
    ensureCapacity(newSize);

    if (byteArrayValue == null) {
        Arrays.fill(data, size, newSize, (byte) 0);
    } else {
        if (byteOffset < 0) {
            throw new IllegalArgumentException("byteOffset < 0");
        }
        if (byteOffset + byteLength > byteArrayValue.length) {
            throw new IllegalArgumentException("byteOffset + byteLength exceeds array length");
        }
        System.arraycopy(byteArrayValue, byteOffset, data, size, byteLength);
    }

    size = newSize;
    return this;
}
}
