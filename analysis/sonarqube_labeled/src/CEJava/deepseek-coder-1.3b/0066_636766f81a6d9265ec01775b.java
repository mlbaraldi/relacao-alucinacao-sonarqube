package generated;
public class Generated157f4a2d9370 {
public long readLong(final int offset){
    return ((long) (bytes[offset + 0] & 0xff) << 56) |
           ((long) (bytes[offset + 1] & 0xff) << 48) |
           ((long) (bytes[offset + 2] & 0xff) << 40) |
           ((long) (bytes[offset + 3] & 0xff) << 32) |
           ((long) (bytes[offset + 4] & 0xff) << 24) |
           ((long) (bytes[offset + 5] & 0xff) << 16) |
           ((long) (bytes[offset + 6] & 0xff) << 8) |
           ((long) (bytes[offset + 7] & 0xff));
}
}
