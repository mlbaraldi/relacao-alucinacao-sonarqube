package generated;
public class Generatedc0c2253dd3ff {
public short readShort(final int offset){
    return (short) ((bytes[offset] & 0xFF) | ((bytes[offset + 1] & 0xFF) << 8));
}
}
