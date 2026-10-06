package generated;
public class Generated157f4a2d9370 {
public long readLong(final int offset){
    long value = 0;
    for (int i = 0; i < 8; i++) {
        value |= (long) readByte(offset + i) << (8 * i);
    }
    return value;
}
}
