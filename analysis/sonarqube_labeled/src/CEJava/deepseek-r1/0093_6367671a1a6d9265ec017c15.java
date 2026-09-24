package generated;
public class Generated630c6f526a77 {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    if (byteLength < 0) {
        throw new IllegalArgumentException("byteLength must be non-negative");
    }
    if (byteLength == 0) {
        return this;
    }

    int newPosition = position + byteLength;
    if (newPosition > buffer.length) {
        buffer = Arrays.copyOf(buffer, Math.max(buffer.length * 2, newPosition));
    }

    if (byteArrayValue == null) {
        Arrays.fill(buffer, position, newPosition, (byte) 0);
    } else {
        System.arraycopy(byteArrayValue, byteOffset, buffer, position, byteLength);
    }

    position = newPosition;
    return this;
}
}
