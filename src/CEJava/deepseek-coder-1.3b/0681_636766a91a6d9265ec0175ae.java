package generated;
public class Generated2258a3c2deaa {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    if (byteArrayValue == null) {
        byteArrayValue = new byte[1];
        byteArrayValue[0] = 0;
    }

    if (byteLength < 0) {
        throw new IllegalArgumentException("byteLength must be >= 0");
    }

    if (byteOffset < 0 || byteOffset > byteArrayValue.length) {
        throw new IllegalArgumentException("byteOffset must be >= 0 and <= byteArrayValue.length");
    }

    if (byteLength == 0) {
        return this;
    }

    int newSize = size() + byteLength;
    if (newSize > capacity()) {
        ensureCapacity(newSize);
    }

    System.arraycopy(byteArrayValue, byteOffset, data, size(), byteLength);
    this.size = newSize;

    return this;
}
}
