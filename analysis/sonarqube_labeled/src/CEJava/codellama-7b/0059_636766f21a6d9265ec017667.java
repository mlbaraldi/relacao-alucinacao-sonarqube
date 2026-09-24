package generated;
public class Generatedc0c2253dd3ff {
public short readShort(final int offset){
    // Check if the offset is within the bounds of the ClassReader
    if (offset < 0 || offset >= this.length) {
        throw new IndexOutOfBoundsException("Offset " + offset + " is outside of the bounds of the ClassReader");
    }

    // Read the short value from the specified offset
    return (short) (this.bytes[offset] << 8 | this.bytes[offset + 1]);
}
}
