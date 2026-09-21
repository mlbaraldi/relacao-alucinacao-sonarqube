package generated;
public class Generated630c6f526a77 {
public ByteVector putByteArray(final byte[] byteArrayValue,final int byteOffset,final int byteLength){
    // Check if byteArrayValue is null
    if (byteArrayValue == null) {
        // If it is, add nullbytes to the byte vector
        for (int i = 0; i < byteLength; i++) {
            this.byteVector.add(Byte.valueOf((byte) 0));
        }
        return this.byteVector;
    }

    // Check if byteOffset and byteLength are valid
    if (byteOffset < 0 || byteLength < 0 || byteOffset + byteLength > byteArrayValue.length) {
        throw new IllegalArgumentException("Invalid byteOffset or byteLength");
    }

    // Check if the byte vector is already large enough to hold the bytes
    if (this.byteVector.size() + byteLength > this.byteVector.capacity()) {
        // If not, double the capacity of the byte vector
        this.byteVector.setCapacity(this.byteVector.size() + byteLength);
    }

    // Copy the bytes from byteArrayValue into the byte vector
    System.arraycopy(byteArrayValue, byteOffset, this.byteVector.toArray(), this.byteVector.size(), byteLength);

    return this.byteVector;
}
}
