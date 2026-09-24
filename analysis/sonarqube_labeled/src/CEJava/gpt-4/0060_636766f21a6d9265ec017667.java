package generated;
public class Generatedc0c2253dd3ff {
public short readShort(final int offset){
    int high = b[offset] & 0xff;
    int low = b[offset + 1] & 0xff;
    return (short) ((high << 8) | low);
}
}
