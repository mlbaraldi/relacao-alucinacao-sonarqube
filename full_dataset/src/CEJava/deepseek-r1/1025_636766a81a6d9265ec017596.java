package generated;
public class Generated7746ec4e0a66 {
public ByteVector putInt(final int intValue){
    ensureCapacity(length + 4);
    data[length++] = (byte) (intValue >> 24);
    data[length++] = (byte) (intValue >> 16);
    data[length++] = (byte) (intValue >> 8);
    data[length++] = (byte) intValue;
    return this;
}
}
